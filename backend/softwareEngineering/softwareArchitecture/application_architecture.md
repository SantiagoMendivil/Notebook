# Table of contents 
- [Table of contents](#table-of-contents)
- [Component](#component)
  - [Component-based Architecture](#component-based-architecture)
- [Services](#services)
  - [Service-oriented Architecture](#service-oriented-architecture)

# Component 
A component is an individual unit of encapsulated functionality. It serves as a part of an application in conjuntion with other components. 

Components should be: 
1. Reusable: Reused in different applications
2. Replaceable: Easily replaced with another component 
3. Independent: Doesn't have dependencies on other components 
4. Extensible: Add behavior without changing other components 
5. Encapsulated: Doesn't expose its specific implementation
6. Non-context specific: Operates in different environments

Examples are: 
1. APIs
2. Data Access Object 
3. Controllers


## Component-based Architecture 
Decomposes design into logical components. Higher levels abstraction than objects. It defines, composes, and implements loosely coupled independent components so they work together to create an application.

# Services 
They are designed to be deployed independently and reused by multiple systems. Has one unique, always running instance. A service is a component that can be deployed independently. 

## Service-oriented Architecture
Loosely coupled services that communicate over a network. Supports building distributed systems that deliver services to other applications through a communication protocol. 
