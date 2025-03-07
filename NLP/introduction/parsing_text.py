"""Parsing text

Once a text was preprocessed (Check on text_processing.py) now it will be helpful
to know how the words are related to each other. 
Parsing is an NLP process concerned with segmenting text based on syntax

NLTK provides methods to make this process easier 

- Part-of-speech-tagging (POS tagging) identified parts of speech like verbs, nouns, adjectives
- Named entity recognition (NER) helps identify the proper nouns in a text. 
- Dependency grammar trees help you understand the relationship between the words in a sentence. spaCy is a 
library that helps us in this point 

"""
import spacy
from nltk import Tree

squids_text = "So many squids are jumping out of suitcases these days. You can barely go anywhere without seeing one. I went to the dentist the other day. Sure enough, I saw an angry one jump out of my dentist's bag. She hardly even noticed."

dependency_parser = spacy.load('en')

parsed_squids = dependency_parser(squids_text)

my_sentence = "I am a very happy person!"
my_parsed_sentence = dependency_parser(my_sentence)

def to_nltk_tree(node):
  if node.n_lefts + node.n_rights > 0:
    parsed_child_nodes = [to_nltk_tree(child) for child in node.children]
    return Tree(node.orth_, parsed_child_nodes)
  else:
    return node.orth_

for sent in parsed_squids.sents:
  to_nltk_tree(sent.root).pretty_print()
  
for sent in my_parsed_sentence.sents:
 to_nltk_tree(sent.root).pretty_print()