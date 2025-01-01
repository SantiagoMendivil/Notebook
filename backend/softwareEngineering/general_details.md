# Table of contents 
- [Table of contents](#table-of-contents)
- [What is Software Engineering?](#what-is-software-engineering)
- [CASE Tools](#case-tools)
- [SDLC: Software Development Life Cycle](#sdlc-software-development-life-cycle)
  - [Introduction](#introduction)
  - [Phases of SDLC](#phases-of-sdlc)
    - [Planning](#planning)
      - [Prototyping](#prototyping)
      - [Software Requirements Specification](#software-requirements-specification)
    - [Design](#design)
    - [Development](#development)
    - [Testing](#testing)
    - [Deployment](#deployment)
    - [Maintenance](#maintenance)
- [Building Good Quality Software](#building-good-quality-software)
  - [Software Processes](#software-processes)
    - [Requirements Gathering](#requirements-gathering)
      - [Requirements Documentation](#requirements-documentation)
    - [Design](#design-1)
    - [Coding for Quality](#coding-for-quality)
    - [Testing](#testing-1)
    - [Releases](#releases)
    - [Documenting](#documenting)

# What is Software Engineering? 
Application of scientific principles to the design and creation of software. The field uses a systematic approach to collect and analyze business requirements in order
to design, build, and test software applications to satisfy those business requirements. 

The responsibilities of a software engineer include: 
1. Designing, building, and maintaining software systems. 
2. Writing and testing code.
3. Cosnulting with stakeholders, third party vendors, security specialists, and other team members .

# CASE Tools 
This stands for Computer-Aided Software Engineering. CASE tools can be divided into six categories:

1. Business Analysis and Modeling. 
2. Development tools such as debugging environments. 
3. Verification and validation tools.
4. Configuration management.
5. Metrics and measurement.
6. Project management.


# SDLC: Software Development Life Cycle
## Introduction 
Is a systematic process to develop high-quality software in a predictable timeframe and budget. The goal of the SDLC is to produce software that meets a client's business requirements. It is defined with their own processes and deliverables. Is a cycle of planning, design and development minimizing development risks and costs. 

Some of the advantages that this process has are 
1. Improves efficiency and reduce risks 
2. Team members know what they should be working on and when
3. Facilitates communication among stakeholders 
4. Team members know when development can move to another phase 
5. Respond to changing requirements 
6. Solve problems early in the process. 
7. Reduces overlapping responsibilities. 


## Phases of SDLC 
### Planning 
Requirements are: 
- Gathered 
- Analyzed 
- Documented 
- Prioritized 

When planning a software solution, the following factors must be considered: users of the solution the overall purpose of the solution, data inputs and outputs, legal and regulatory compliance, risk identification, quality assurance requirements, allocation of human and financial resources, and project scheduling.

Labor and material costs are estimated and weighed against time constaints. 

#### Prototyping 
A prototype is a small-scale stage replica of the end product used to get stakeholder feedback and establish requirements. Tests design ideas and can be developed at various stages when we have to modify the requirements. 

#### Software Requirements Specification 
The SRS called Software Requirements Specification is where all the system requirements are documented and needs to be clearly understood and approved by all the stakeholders. 

### Design 
Requirements are gathered from the SRS to develop architecture. In this phase we follow all the requirements in order to produce the design of the software. 

### Development 
In this phase we start implementing all the design that we gave into the system

### Testing 
Once the coding is complete (If its TDD then it will be at the same time as the development) we start testing as: 
- Unit testing 
- Integration testing
- System testing 
- Acceptanse testing

### Deployment 
Where the application is released into the production environment and is presented to the final users. This approach can be used for making software available on a website, mobile device app store, or a software distribution server on a corporate network. 

### Maintenance
This phase helps to find any other busgs, identify user interface issues, or UI for short, and identify other requirements that may not have been listed in the SRS. 


# Building Good Quality Software 
## Software Processes 
### Requirements Gathering
The SRS encompasses the process of collecting and documenting the set of requirements that the software needs to adhere to. It may include use cases. 

There is a six-step process of defining a problem to be solved and documenting how to go about solving that problem: 

1. Identifying stakeholders
2. Establishing goals and objectives 
3. Eliciting requirements from the stakeholders
4. Documenting the requirements 
5. Analyzing and confirming the requirements 
6. Prioritizing the requirements (Must-Have, Highly Desired, Nice to Have).

#### Requirements Documentation 
From the requirements that we gather in this process we will get three types of documentation for a project, which are: 

1. Software Requirements Specification(SRS): Includes a purpose statement that contains the intended use of the SRS(**Who has access to the SRS and how it should be used**), its audience and scope(**Describes the software benefits, goals and objectives**), constraints(**How the software must operate under given conditions**), assumptions and dependencies(**Required OS or hardware or other software products**), and requirements which can be divided into the following sections. 
   1. Functional (Functions of the software)
   2. External & User Interface (Users and interaction with other hardware or software)
   3. System Features (Functions of the system)
   4. Non functional (Performance, safety, security and quality)

2. User Requirements Specification(URS): Describe business need and end-user expectation. It uses **User Stories** which ask who is the user? What is the function that needs to be performed, and why does the user want this functionality. This is confirmed during user acceptance testing. 
3. System Requirements Specification(SysRS): Outlines the requirements of the entire system. Is broader than a SRS. It contains system capabilities, interfaces and user characteristics, policy, regulation, performance, security and system acceptance criteria. 

### Design 
Transforming requirements into code. Breaking down requirements into sets of related components. Communicating business rules and application logic. 


### Coding for Quality 
This refers to the characteristics of the code including: 

1. Maintainability
2. Readability
3. Testability
4. Security

The code must be 
1. Clean and consistent 
2. Easy to read and maintain 
3. Well documented 
4. Efficient. 

Important standards.
1. Following coding standards 
2. Using linters to detect errors 
3. Commenting in the code itseld. 



### Testing 
The process of verifying that the software matches established requirements. 


### Releases 
When the newest version of the software is distributed, it is referred to as a "Release". There can be "Alpha"(Select some stakeholdes, the software may have errors; is a preview of the functioning version), "Beta"(All the stakeholders; user testing; meet all the requirements) and "GA"(Stable version; for all the users ) RELEASE. 

### Documenting
System documentation is geared towards the technical user. Technical users may be other engineers, developers, or architects. System documentation explains how the software operates or how to use it. 

User documentation is provided to the non-technical end-users to assist them in the use of the product. Generally is provided in the form of user guides. 

