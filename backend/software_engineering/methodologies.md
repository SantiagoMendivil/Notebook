# Table of contents
- [Table of contents](#table-of-contents)

# Common Development Methodologies 

## Waterfall 
Sequential method in a software development where the output of one phase is the input for the next phase of the cycle. 

All planning is done up front. 

## The V-shape 
The phases going down the left side of the V are called "Verification". Then going up the right side of the V, those phases are called "Validation". In this methodology we have four stages which are planning, system design, architecture design and then the module design. The bottom of the V is the coding phase. And going back up the V are the four phases that correspong to the phases going down the V. 

The tests are written during the verification phases and executed during the validation stages. 

## Agile Model 
It focuses on a collaborative software development process over multiple short cycles rather than a strictly top-down linear process. It is an iterative approach to development where the devirables are known as sprints. 

The four core values of agile development outlined in what is known as the "Agile manifesto" are: 

1. Individuals and interactions over processes and tools
2. Working software over comprehensive documentation 
3. Customer collaboration over contract negotiation 
4. Responding to change over following a plan. 


# Software Versions 
Software versions tell us a lot about programs and applications. User can determine what software version they're using, and developers can provide useful information with version numbers. 

- These are identified by version numbers 
  - When the software was released 
  - When it was updated 
  - If any minor changes or fixes were made to the software. 
- These versions are for keeping track of new software updates and patches. 

# Software Testing 
We use test cases that verify the functionality and requirements from a system. This can be written in different stages of the SDLC, it includes steps, inputs, data and expected output. 

Types of testing: 
1. **Funcitonal**: Involves black box where we set an input and an output where the system is under test between these two in order to get the correct results. It ensures usability and accessibility. 
2. **Non-functional**: Includes performance, security, availability and scalability. Checks if the system is preforming accordingly to the performance requirements.  
3. **Regression testing**: Confirms changes don't break the application. Occurs after fixes such as changes in the requirements. The test cases can contain frequent defects, features with recent changes, complex cases or edge cases. 


## Testing Levels 

### Unit 
- Occurs during the build phase of the SDLC
- Test a module of code 
- Eliminate errors before integration with other modules. 

### Integration
- Identify errors introduced when two or more modules are combined 
- Type of black-box test. 
- Occurs after modules are combined into a larger system

### System 
- Occurs after integration testing 
- Compliance with SRS 
- Validates the system 
- Functional and non-functional testing 
- Staging environment 


### Acceptance
- Formal testing for user needs 
- Asks if the needs of the users, customers and stakeholders is satisfied. 