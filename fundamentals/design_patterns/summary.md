# Design Patterns Summary

---

## Creational Design Patterns

| Pattern Name      | Best Description                                                                 | Best Example to Remember It                |
|-------------------|----------------------------------------------------------------------------------|--------------------------------------------|
| Singleton         | Ensures a class has only one instance and provides a global access point.         | Database connection manager                |
| Factory Method    | Defines an interface for creating objects, letting subclasses decide the type.    | Vehicle factory creating cars/bikes        |
| Abstract Factory  | Provides an interface for creating families of related objects without specifying their concrete classes. | GUI toolkit for Windows/Mac widgets        |
| Builder           | Constructs complex objects step by step, separating construction from representation. | Building a custom computer                 |
| Prototype         | Creates new objects by copying an existing object (cloning).                     | Cloning a document template                |

---

## Structural Design Patterns

| Pattern Name      | Best Description                                                                 | Best Example to Remember It                |
|-------------------|----------------------------------------------------------------------------------|--------------------------------------------|
| Adapter           | Allows incompatible interfaces to work together by converting one interface to another. | Mobile charger adapter (220V to 5V)        |
| Bridge            | Decouples abstraction from implementation so both can vary independently.         | Shape-color pairing (Circle + Red, Square + Green) |
| Composite         | Composes objects into tree structures to represent part-whole hierarchies.        | File system (folders and files)            |
| Decorator         | Adds responsibilities to objects dynamically without altering their structure.    | Coffee with milk and sugar add-ons         |
| Facade            | Provides a simplified interface to a complex subsystem.                          | Home theater remote controlling multiple devices |
| Flyweight         | Shares objects to support large numbers efficiently, minimizing memory usage.     | Characters in a text editor                |
| Proxy             | Provides a surrogate or placeholder for another object to control access.         | Internet proxy server                      |

---

## Behavioral Design Patterns

| Pattern Name      | Best Description                                                                 | Best Example to Remember It                |
|-------------------|----------------------------------------------------------------------------------|--------------------------------------------|
| Strategy          | Defines a family of algorithms, encapsulates each, and makes them interchangeable. | Sorting algorithms (bubble, quick, merge)  |
| Observer          | Allows objects to be notified of state changes in other objects.                  | News agency notifying subscribers          |
| Command           | Encapsulates a request as an object, allowing parameterization and queuing.       | Remote control buttons (undo/redo)         |
| Iterator          | Provides a way to access elements of a collection sequentially without exposing its underlying representation. | Iterating over a list                      |
| Mediator          | Defines an object that centralizes communication between other objects.           | Air traffic control tower                  |
| Memento           | Captures and restores an object's internal state without violating encapsulation. | Undo feature in text editor                |
| State             | Allows an object to alter its behavior when its internal state changes.           | Traffic light switching colors             |
| Template Method   | Defines the skeleton of an algorithm, deferring steps to subclasses.              | Making tea/coffee (boil, brew, pour, add condiments) |
| Visitor           | Separates an algorithm from the objects it operates on, allowing new operations.  | Tax calculation for different products     |
| Chain of Responsibility | Passes a request along a chain of handlers until one handles it.            | Technical support escalation               |
| Interpreter       | Implements a grammar for interpreting expressions.                                | Evaluating mathematical expressions        |

---