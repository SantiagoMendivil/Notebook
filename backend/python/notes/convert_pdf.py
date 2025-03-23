import os
import re
import argparse
import ast
from typing import Dict, List, Tuple, Optional
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, ListFlowable, ListItem
from reportlab.platypus import PageBreak, Image
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT

class PyPDFDocGen:
    """
    Documentation generator for python code only.
    Analyze the comments in the code and extracts them in order to generate the pdf.
    """
    
    def __init__(self, input_dir: str, output_dir: str, style_file: Optional[str] = None):
        """
        Initializes the class.
        
        Args:
            input_dir: Directory with python files to document
            output_dir: Directory to save the generated PDF
            style_file: Optional styles file for the PDF
        """
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.style_file = style_file
        self.files_data = {}        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Initializes the styles for the PDF
        self.styles = getSampleStyleSheet()
        self.init_custom_styles()
            
    def init_custom_styles(self):
        """
        Initializes custom styles for the PDF
        """
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Title'],
            fontSize=24,
            alignment=TA_CENTER,
            spaceAfter=24,
            textColor=colors.darkblue
        ))
        
        # Heading styles
        self.styles.add(ParagraphStyle(
            name='CustomHeading1',
            parent=self.styles['Heading1'],
            fontSize=18,
            textColor=colors.darkblue,
            spaceBefore=12,
            spaceAfter=6,
            borderWidth=0,
            borderPadding=5,
            borderColor=colors.lightgrey,
            borderRadius=5
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomHeading2',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.navy,
            spaceBefore=10,
            spaceAfter=6,
            leftIndent=5
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomHeading3',
            parent=self.styles['Heading3'],
            fontSize=14,
            textColor=colors.darkblue,
            spaceBefore=8,
            spaceAfter=4,
            leftIndent=10
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomHeading4',
            parent=self.styles['Heading4'],
            fontSize=12,
            textColor=colors.darkblue,
            spaceBefore=6,
            spaceAfter=3,
            leftIndent=15,
            backColor=colors.lightgrey,
            borderPadding=3
        ))
        
        # Style for documentation 
        self.styles.add(ParagraphStyle(
            name='DocString',
            parent=self.styles['Normal'],
            leftIndent=20,
            spaceAfter=6,
            fontName='Helvetica-Oblique',
            textColor=colors.darkslategray
        ))
        
        # Style for list items 
        self.styles.add(ParagraphStyle(
            name='ListItem',
            parent=self.styles['Normal'],
            leftIndent=30,
            bulletIndent=15,
            spaceBefore=2,
            spaceAfter=2
        ))
        
        # Style for parameters, returns, and exceptions
        self.styles.add(ParagraphStyle(
            name='ParamItem',
            parent=self.styles['Normal'],
            leftIndent=40,
            firstLineIndent=-15,
            spaceBefore=1,
            spaceAfter=1,
            textColor=colors.darkslategray
        ))
        
        # Style for section label
        self.styles.add(ParagraphStyle(
            name='SectionLabel',
            parent=self.styles['Normal'],
            leftIndent=20,
            spaceBefore=6,
            spaceAfter=2,
            fontName='Helvetica-Bold',
            textColor=colors.darkblue
        ))
        
        # Style for table of contents items
        self.styles.add(ParagraphStyle(
            name='TOCItem',
            parent=self.styles['Normal'],
            leftIndent=20,
            firstLineIndent=-15,
            spaceBefore=1,
            spaceAfter=1
        ))
            
    def parse_file(self, file_path: str) -> Dict:
        """
        Analyze a python file and extract the documentation.
        
        Args:
            file_path: Route to the python file.
            
        Returns:
            Dictionary with the python's file information. 
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        file_data = {
            'file_name': os.path.basename(file_path),
            'module_doc': '',
            'classes': [],
            'functions': []
        }
        try:
            tree = ast.parse(content)            
            if tree.body and isinstance(tree.body[0], ast.Expr) and isinstance(tree.body[0].value, ast.Constant):
                file_data['module_doc'] = tree.body[0].value.s.strip()            
            for node in tree.body:
                if isinstance(node, ast.ClassDef):
                    class_info = self._process_class(node)
                    file_data['classes'].append(class_info)                
                elif isinstance(node, ast.FunctionDef):
                    func_info = self._process_function(node)
                    file_data['functions'].append(func_info)  
        except SyntaxError as e:
            print(f"Error analyzing {file_path}: {e}")
        return file_data
    
    def _process_class(self, node: ast.ClassDef) -> Dict:
        """
        Process a class's node and extract the documentation.
        
        Args:
            node: Ast node of the class.
            
        Returns:
            Dictionary with the class's information. 
        """
        class_info = {
            'name': node.name,
            'doc': self._get_docstring(node),
            'methods': [],
            'base_classes': [self._get_name(base) for base in node.bases]
        }
        # Process the methods in the class 
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                method_info = self._process_function(item)
                class_info['methods'].append(method_info) 
        return class_info
    
    def _process_function(self, node: ast.FunctionDef) -> Dict:
        """
        Process a method's information and extracts the documentation.
        
        Args:
            node: Ast node for the method.
            
        Returns:
            Dictionary with the method's information. 
        """
        # Extract parameters information 
        params = []
        for arg in node.args.args:
            param_name = arg.arg
            param_type = ''
            # Verify the arg type
            if arg.annotation:
                param_type = self._get_annotation(arg.annotation)
            params.append({'name': param_name, 'type': param_type})
        # Extract return types
        return_type = ''
        if node.returns:
            return_type = self._get_annotation(node.returns)
        
        # Get the full docstring first
        full_docstring = self._get_docstring(node)
        
        # Process the docstring to extract parameters and returns types
        main_doc, param_docs, return_doc, exceptions_doc = self._parse_docstring(full_docstring)
        
        # Combine the parameter's information and their documentation
        for param in params:
            if param['name'] in param_docs:
                param['doc'] = param_docs[param['name']]
        return {
            'name': node.name,
            'doc': main_doc,  # Only the main part of the docstring
            'params': params,
            'return_type': return_type,
            'return_doc': return_doc,
            'exceptions': exceptions_doc,
            'decorators': [self._get_name(d) for d in node.decorator_list]
        }
    
    def _get_docstring(self, node) -> str:
        """
        Extracts the doscstring from an AST's node.
        
        Args:
            node: AST node (Class or Method)
            
        Returns:
            Docstring extracted
        """
        for item in node.body:
            if isinstance(item, ast.Expr) and isinstance(item.value, ast.Constant):
                return item.value.s.strip()
        return ''
    
    def _parse_docstring(self, docstring: str) -> Tuple[str, Dict[str, str], str, List[Dict[str, str]]]:
        """
        Parse the docstring to separate the main description from parameters, returns, and exceptions.
        
        Args:
            docstring: The full docstring to parse
            
        Returns:
            Tuple containing:
            - Main description
            - Parameters dictionary
            - Return documentation
            - Exceptions list
        """
        main_doc = docstring
        
        # Extract parameters section
        param_pattern = r'\n\s*(?:Args|Parameters):\s*\n'
        sections = re.split(param_pattern, docstring, maxsplit=1)
        if len(sections) > 1:
            main_doc = sections[0].strip()
            rest = sections[1]
        else:
            rest = ""
            
        # If other sections exist, continue parsing the rest
        return_pattern = r'\n\s*(?:Returns|Return):\s*\n'
        exc_pattern = r'\n\s*(?:Raises|Exceptions):\s*\n'
        
        param_docs = self._extract_param_docs(docstring)
        return_doc = self._extract_return_doc(docstring)
        exceptions_doc = self._extract_exceptions_doc(docstring)
        
        return main_doc, param_docs, return_doc, exceptions_doc
    
    def _get_name(self, node) -> str:
        """
        Get an AST node's name.
        
        Args:
            node: AST node
            
        Returns:
            Name extracted
        """
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return f"{self._get_name(node.value)}.{node.attr}"
        elif isinstance(node, ast.Call):
            return self._get_name(node.func)
        return str(node)
    
    def _get_annotation(self, node) -> str:
        """
        Extract the annotation from an AST node .
        
        Args:
            node: AST Node
            
        Returns:
            Annotation of type extracted
        """
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return f"{self._get_name(node.value)}.{node.attr}"
        elif isinstance(node, ast.Subscript):
            base = self._get_name(node.value)
            if isinstance(node.slice, ast.Index):
                # For python 3.8-
                if hasattr(node.slice, 'value'):
                    if isinstance(node.slice.value, ast.Tuple):
                        slice_str = ", ".join([self._get_name(e) for e in node.slice.value.elts])
                    else:
                        slice_str = self._get_name(node.slice.value)
                else:
                    # For python 3.9+
                    if isinstance(node.slice, ast.Tuple):
                        slice_str = ", ".join([self._get_name(e) for e in node.slice.elts])
                    else:
                        slice_str = self._get_name(node.slice)
                return f"{base}[{slice_str}]"
        return str(node)
    
    def _extract_param_docs(self, docstring: str) -> Dict[str, str]:
        """
        Extract the parameters from a docstring.
        
        Args:
            docstring: Docstring to analyze
            
        Returns:
            Dictionaty with paramethers extracted 
        """
        param_docs = {}
        # Pattern of "Args" or "Parameters" followed by the description
        sections = re.split(r'\n\s*(?:Args|Parameters):\s*\n', docstring, maxsplit=1)
        if len(sections) > 1:
            params_section = sections[1].split('\n\n')[0]
            param_lines = params_section.strip().split('\n')
            current_param = None
            current_desc = []
            for line in param_lines:
                # Verfiy if there is a new line on the parameters 
                param_match = re.match(r'^\s*(\w+)(?:\s*\(\w+\))?\s*:\s*(.*)$', line)
                if param_match:
                    # Save the previous parameter if exists
                    if current_param:
                        param_docs[current_param] = '\n'.join(current_desc).strip()
                    # Initialize a new parameter
                    current_param = param_match.group(1)
                    current_desc = [param_match.group(2)]
                elif current_param and line.strip():
                    # Continue with the actual description of the parameter
                    current_desc.append(line.strip())
            # Save the last parameter if exists
            if current_param:
                param_docs[current_param] = '\n'.join(current_desc).strip()
                
        return param_docs
    
    def _extract_return_doc(self, docstring: str) -> str:
        """
        Extract the information about the returns in the docstring.
        
        Args:
            docstring: Docstring to analyze
            
        Returns:
            Documentation of return type
        """
        sections = re.split(r'\n\s*(?:Returns|Return):\s*\n', docstring, maxsplit=1)
        if len(sections) > 1:
            return_section = sections[1].split('\n\n')[0].strip()
            return return_section
        return ''
    
    def _extract_exceptions_doc(self, docstring: str) -> List[Dict[str, str]]:
        """
        Extract the exceptions information in the docstring.
        
        Args:
            docstring: Docstring to analyze
            
        Returns:
            List of documented exceptions.
        """
        exceptions = []
        sections = re.split(r'\n\s*(?:Raises|Exceptions):\s*\n', docstring, maxsplit=1)
        if len(sections) > 1:
            raises_section = sections[1].split('\n\n')[0]
            raises_lines = raises_section.strip().split('\n')
            current_exc = None
            current_desc = []
            for line in raises_lines:
                # Verify if there is a new line on the exceptions 
                exc_match = re.match(r'^\s*(\w+)(?:\s*\(\w+\))?\s*:\s*(.*)$', line)
                if exc_match:
                    # Save the previous exception if exists
                    if current_exc:
                        exceptions.append({'type': current_exc, 'description': '\n'.join(current_desc).strip()})
                    # Initialize a new exception documentation
                    current_exc = exc_match.group(1)
                    current_desc = [exc_match.group(2)]
                elif current_exc and line.strip():
                    # Continue with the actual description of the exception
                    current_desc.append(line.strip())
            # Save the last exception if exists
            if current_exc:
                exceptions.append({'type': current_exc, 'description': '\n'.join(current_desc).strip()})     
        return exceptions
        
    def process_directory(self):
        """
        Process all files for the directory.
        """
        for root, _, files in os.walk(self.input_dir):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    file_path = os.path.join(root, file)
                    print(f"Processing: {file_path}")
                    try:
                        relative_path = os.path.relpath(file_path, self.input_dir)
                        self.files_data[relative_path] = self.parse_file(file_path)
                    except Exception as e:
                        print(f"Error processing {file_path}: {e}")
    
    def generate_pdf(self):
        """
        Generates a single PDF containing documentation for all processed files.
        """
        output_path = os.path.join(self.output_dir, 'documentation.pdf')
        
        # Create PDF with custom styling
        doc = SimpleDocTemplate(
            output_path, 
            pagesize=letter,
            leftMargin=0.75*inch,
            rightMargin=0.75*inch,
            topMargin=0.75*inch,
            bottomMargin=0.75*inch,
            title="Python Code Documentation"
        )
        
        story = []
        
        # Title and introduction
        story.append(Paragraph("Python Code Documentation", self.styles['CustomTitle']))
        story.append(Spacer(1, 12))
        
        # Introduction with better styling
        intro_text = """<para>This document contains the automatically generated documentation for all Python files in the project. 
        The documentation is extracted from docstrings and type annotations in the code.</para>"""
        story.append(Paragraph(intro_text, self.styles['Normal']))
        story.append(Spacer(1, 24))
        
        # Table of Contents with better styling
        story.append(Paragraph("Table of Contents", self.styles['CustomHeading1']))
        story.append(Spacer(1, 12))
        
        # List all files in the table of contents with better structure
        toc_data = []
        for file_path in sorted(self.files_data.keys()):
            file_data = self.files_data[file_path]
            story.append(Paragraph(f"• <b>{file_path}</b>", self.styles['TOCItem']))
            
            # Classes TOC
            if file_data['classes']:
                for cls in file_data['classes']:
                    story.append(Paragraph(f"   - Class: {cls['name']}", self.styles['TOCItem']))
            
            # Functions TOC
            if file_data['functions']:
                for func in file_data['functions']:
                    story.append(Paragraph(f"   - Function: {func['name']}", self.styles['TOCItem']))
        
        story.append(PageBreak())
        
        # Generate documentation for each file with improved styling
        for file_path in sorted(self.files_data.keys()):
            file_data = self.files_data[file_path]
            
            # Add file header with styled box
            story.append(Paragraph(f"Module: {file_path}", self.styles['CustomHeading1']))
            
            # Module documentation with better styling
            if file_data['module_doc']:
                story.append(Paragraph(file_data['module_doc'], self.styles['DocString']))
                story.append(Spacer(1, 12))
            
            # Content table for this file
            story.append(Paragraph("Content", self.styles['CustomHeading2']))
            story.append(Spacer(1, 6))
            
            # Content table for classes
            if file_data['classes']:
                story.append(Paragraph("Classes", self.styles['CustomHeading3']))
                for cls in file_data['classes']:
                    story.append(Paragraph(f"• {cls['name']}", self.styles['ListItem']))
                story.append(Spacer(1, 6))
                
            # Content table for methods 
            if file_data['functions']:
                story.append(Paragraph("Functions", self.styles['CustomHeading3']))
                for func in file_data['functions']:
                    story.append(Paragraph(f"• {func['name']}", self.styles['ListItem']))
                story.append(Spacer(1, 12))
            
            # Generate documentation for classes with better styling
            if file_data['classes']:
                story.append(Paragraph("Classes", self.styles['CustomHeading2']))
                story.append(Spacer(1, 6))
                
                for cls in file_data['classes']:
                    # Class name with colored background
                    story.append(Paragraph(cls['name'], self.styles['CustomHeading3']))
                    
                    # Base classes with better styling
                    if cls['base_classes']:
                        base_classes_str = ', '.join(cls['base_classes'])
                        story.append(Paragraph(f"<i><b>Inherits from:</b> {base_classes_str}</i>", 
                                               self.styles['Normal']))
                    
                    # Class docstring with proper indentation
                    if cls['doc']:
                        story.append(Paragraph(cls['doc'], self.styles['DocString']))
                        story.append(Spacer(1, 6))
                    
                    # Document methods with better styling
                    if cls['methods']:
                        story.append(Paragraph("Methods", self.styles['CustomHeading4']))
                        for method in cls['methods']:
                            method_elements = self._generate_function_elements(method, is_method=True)
                            story.extend(method_elements)
                            
                    story.append(Spacer(1, 12))
            
            # Generate method's documentation with better styling
            if file_data['functions']:
                story.append(Paragraph("Functions", self.styles['CustomHeading2']))
                story.append(Spacer(1, 6))
                
                for func in file_data['functions']:
                    func_elements = self._generate_function_elements(func)
                    story.extend(func_elements)
            
            # Add page break between files
            if file_path != sorted(self.files_data.keys())[-1]:  # Don't add page break after last file
                story.append(PageBreak())
                
        # Build the PDF
        doc.build(story)
        print(f"Documentation generated at {output_path}")
    
    def _generate_function_elements(self, func: Dict, is_method: bool = False) -> List:
        """
        Generate PDF elements for the function.
        
        Args:
            func: Function data
            is_method: Indicates if it's a class's method
            
        Returns:
            Elements list for the pdf
        """
        elements = []
        
        # Name and signature with better styling
        params_str = ', '.join([f"{p['name']}: {p['type']}" if p['type'] else p['name'] for p in func['params']])
        return_str = f" → {func['return_type']}" if func['return_type'] else ""
        
        # Function signature with styled background
        elements.append(Paragraph(f"{func['name']}({params_str}){return_str}", self.styles['CustomHeading4']))
        
        # Decorators with better styling
        if func['decorators']:
            decorators_str = ', '.join([f'@{d}' for d in func['decorators']])
            elements.append(Paragraph(f"<i><b>Decorators:</b> {decorators_str}</i>", self.styles['Normal']))
        
        # General documentation with better styling
        if func['doc']:
            elements.append(Paragraph(func['doc'], self.styles['DocString']))
        
        # Parameters with better styling
        if func['params']:
            elements.append(Paragraph("Parameters", self.styles['SectionLabel']))
            for param in func['params']:
                param_text = f"<b>{param['name']}</b>"
                if param['type']:
                    param_text += f" <i>({param['type']})</i>"
                if 'doc' in param and param['doc']:
                    param_text += f": {param['doc']}"
                elements.append(Paragraph(param_text, self.styles['ParamItem']))
        
        # Return values with better styling
        if func['return_doc'] or func['return_type']:
            elements.append(Paragraph("Returns", self.styles['SectionLabel']))
            return_text = ""
            if func['return_type']:
                return_text += f"<b>{func['return_type']}</b>"
            if func['return_doc']:
                if func['return_type']:
                    return_text += ": "
                return_text += func['return_doc']
            elements.append(Paragraph(return_text, self.styles['ParamItem']))
        
        # Exceptions with better styling
        if func['exceptions']:
            elements.append(Paragraph("Exceptions", self.styles['SectionLabel']))
            for exc in func['exceptions']:
                exc_text = f"<b>{exc['type']}</b>"
                if exc['description']:
                    exc_text += f": {exc['description']}"
                elements.append(Paragraph(exc_text, self.styles['ParamItem']))
        
        elements.append(Spacer(1, 12))
        return elements

def main():
    parser = argparse.ArgumentParser(description='Python documentation generator')
    parser.add_argument('input', help='Directory with python docs to document')
    parser.add_argument('output', help='Directory to save the documentation')
    parser.add_argument('--style', '-s', help='Optional pdf styles')
    
    args = parser.parse_args()
    
    docgen = PyPDFDocGen(args.input, args.output, args.style)
    docgen.process_directory()
    docgen.generate_pdf()  

if __name__ == '__main__':
    main()