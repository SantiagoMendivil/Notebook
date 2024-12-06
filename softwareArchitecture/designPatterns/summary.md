# Summary of Patterns 

## Creational Patterns

### Singleton
- **Purpose**: Ensure a class has only one instance and provide a global point of access to it.
- **When to use**: When exactly one object is needed to coordinate actions across the system.

### Factory Method
- **Purpose**: Define an interface for creating an object, but let subclasses alter the type of objects that will be created.
- **When to use**: When a class cannot anticipate the class of objects it must create.

### Abstract Factory
- **Purpose**: Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
- **When to use**: When the system needs to be independent of how its objects are created.

### Builder
- **Purpose**: Separate the construction of a complex object from its representation so that the same construction process can create different representations.
- **When to use**: When creating complex objects with many optional parts.

### Prototype
- **Purpose**: Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.
- **When to use**: When the classes to instantiate are specified at runtime.

## Structural Patterns

### Adapter
- **Purpose**: Convert the interface of a class into another interface clients expect.
- **When to use**: When you want to use a class that does not have an interface that matches the one you need.

### Bridge
- **Purpose**: Decouple an abstraction from its implementation so that the two can vary independently.
- **When to use**: When you want to avoid a permanent binding between an abstraction and its implementation.

### Composite
- **Purpose**: Compose objects into tree structures to represent part-whole hierarchies.
- **When to use**: When you want to represent part-whole hierarchies of objects.

### Decorator
- **Purpose**: Attach additional responsibilities to an object dynamically.
- **When to use**: When you want to add responsibilities to individual objects without affecting other objects.

### Facade
- **Purpose**: Provide a unified interface to a set of interfaces in a subsystem.
- **When to use**: When you want to provide a simple interface to a complex subsystem.

### Flyweight
- **Purpose**: Use sharing to support large numbers of fine-grained objects efficiently.
- **When to use**: When many objects must be manipulated and storage costs are high.

### Proxy
- **Purpose**: Provide a surrogate or placeholder for another object to control access to it.
- **When to use**: When you need a more versatile or sophisticated reference to an object.

## Behavioral Patterns

### Chain of Responsibility
- **Purpose**: Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request.
- **When to use**: When more than one object may handle a request, and the handler is not known a priori.

### Command
- **Purpose**: Encapsulate a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations.
- **When to use**: When you need to parameterize objects with operations.

### Interpreter
- **Purpose**: Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.
- **When to use**: When you have a language to interpret, and you can represent statements in the language as abstract syntax trees.

### Iterator
- **Purpose**: Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
- **When to use**: When you need to traverse a collection without exposing its internal structure.

### Mediator
- **Purpose**: Define an object that encapsulates how a set of objects interact.
- **When to use**: When you want to reduce the complexity of communication between multiple objects.

### Memento
- **Purpose**: Without violating encapsulation, capture and externalize an object's internal state so that the object can be restored to this state later.
- **When to use**: When you need to save and restore the state of an object.

### Observer
- **Purpose**: Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **When to use**: When an object change should trigger updates to other objects.

### State
- **Purpose**: Allow an object to alter its behavior when its internal state changes.
- **When to use**: When an object's behavior depends on its state, and it must change behavior at runtime.

### Strategy
- **Purpose**: Define a family of algorithms, encapsulate each one, and make them interchangeable.
- **When to use**: When you need to use different variants of an algorithm.

### Template Method
- **Purpose**: Define the skeleton of an algorithm in an operation, deferring some steps to subclasses.
- **When to use**: When you want to let subclasses redefine certain steps of an algorithm without changing its structure.

### Visitor
- **Purpose**: Represent an operation to be performed on the elements of an object structure.
- **When to use**: When you need to perform operations across a set of objects with different interfaces.