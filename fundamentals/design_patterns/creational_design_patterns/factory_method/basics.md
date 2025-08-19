# Factory Method Design Pattern  
_Last Updated : 23 Jul, 2025_

---

The Factory Method Design Pattern is a creational design pattern that provides an interface for creating objects in a superclass, allowing subclasses to alter the type of objects that will be created. This pattern is particularly useful when the exact types of objects to be created may vary or need to be determined at runtime, enabling flexibility and extensibility in object creation.

---

## Table of Content

- What is the Factory Method Design Pattern?
- When to use Factory Method Design Pattern?
- Components of Factory Method Design Pattern
- Factory Method Design Pattern Example
- Use Cases of the Factory Method Design Pattern
- Advantages of Factory Method Design Pattern
- Disadvantages of Factory Method Design Pattern

---

## What is the Factory Method Design Pattern?

The Factory Method Design Pattern is a creational design pattern used in software development. It provides an interface for creating objects in a superclass while allowing subclasses to specify the types of objects they create.

This pattern simplifies the object creation process by placing it in a dedicated method, promoting loose coupling between the object creator and the objects themselves.  
This approach enhances flexibility, extensibility, and maintainability, enabling subclasses to implement their own factory methods for creating specific object types.

---

## When to Use the Factory Method Design Pattern

- If your object creation process is complex or varies under different conditions, using a factory method can make your client code simpler and promote reusability.
- The Factory Method Pattern allows you to create objects through an interface or abstract class, hiding the details of concrete implementations. This reduces dependencies and makes it easier to modify or expand the system without affecting existing code.
- If your application needs to create different versions of a product or may introduce new types in the future, the Factory Method Pattern provides a flexible way to handle these variations by defining specific factory methods for each product type.
- Factories can also encapsulate configuration logic, allowing clients to customize the object creation process by providing parameters or options to the factory method.

---

## Components of Factory Method Design Pattern

- **Creator:** An abstract class or interface that declares the factory method. The creator typically contains a method that serves as a factory for creating objects. It may also contain other methods that work with the created objects.
- **Concrete Creator:** Subclasses of the Creator that implement the factory method to create specific types of objects. Each Concrete Creator is responsible for creating a particular product.
- **Product:** The interface or abstract class for the objects that the factory method creates. The Product defines the common interface for all objects that the factory method can create.
- **Concrete Product:** The actual objects that the factory method creates. Each Concrete Product class implements the Product interface or extends the Product abstract class.

---

## Factory Method Design Pattern Example

**Problem Statement:**  
Consider a software application that needs to handle the creation of various types of vehicles, such as Two Wheelers, Three Wheelers, and Four Wheelers. Each type of vehicle has its own specific properties and behaviors.

### 1. Without Factory Method Design Pattern

```java
// Library classes
abstract class Vehicle {
    public abstract void printVehicle();
}

class TwoWheeler extends Vehicle {
    public void printVehicle() {
        System.out.println("I am two wheeler");
    }
}

class FourWheeler extends Vehicle {
    public void printVehicle() {
        System.out.println("I am four wheeler");
    }
}

// Client (or user) class
class Client {
    private Vehicle pVehicle;

    public Client(int type) {
        if (type == 1) {
            pVehicle = new TwoWheeler();
        } else if (type == 2) {
            pVehicle = new FourWheeler();
        } else {
            pVehicle = null;
        }
    }

    public void cleanup() {
        if (pVehicle != null) {
            pVehicle = null;
        }
    }

    public Vehicle getVehicle() {
        return pVehicle;
    }
}

// Driver program
public class GFG {
    public static void main(String[] args) {
        Client pClient = new Client(1);
        Vehicle pVehicle = pClient.getVehicle();
        if (pVehicle != null) {
            pVehicle.printVehicle();
        }
        pClient.cleanup();
    }
}
```

**Output:**
```
I am two wheeler
```

#### Issues with the Current Design

- The Client class creates TwoWheeler and FourWheeler objects directly based on input. This strong dependency makes the code hard to maintain or update.
- The Client class not only decides which vehicle to create but also handles its lifecycle. This mixes responsibilities, which goes against the principle that a class should only have one reason to change.
- To add a new vehicle type, you must modify the Client class, which makes it difficult to scale the design. This conflicts with the idea that classes should be open for extension but closed for modification.

#### Solutions to the Problems

- **Define a Factory Interface:** Create an interface, VehicleFactory, with a method to produce vehicles.
- **Create Specific Factories:** Implement classes like TwoWheelerFactory and FourWheelerFactory that follow the VehicleFactory interface, providing methods for each vehicle type.
- **Revise the Client Class:** Change the Client class to use a VehicleFactory instance instead of creating vehicles directly. This way, it can request vehicles without using conditional logic.
- **Enhance Flexibility:** This structure allows for easy addition of new vehicle types by simply creating new factory classes, without needing to alter existing Client code.

---

### 2. With Factory Method Design Pattern

#### 1. Product Interface

```java
// Product interface representing a vehicle
public abstract class Vehicle {
    public abstract void printVehicle();
}
```

#### 2. Concrete Products

```java
// Concrete product classes representing different types of vehicles
public class TwoWheeler extends Vehicle {
    public void printVehicle() {
        System.out.println("I am two wheeler");
    }
}

public class FourWheeler extends Vehicle {
    public void printVehicle() {
        System.out.println("I am four wheeler");
    }
}
```

#### 3. Creator Interface (Factory Interface)

```java
// Factory interface defining the factory method
public interface VehicleFactory {
    Vehicle createVehicle();
}
```

#### 4. Concrete Creators (Concrete Factories)

```java
// Concrete factory class for TwoWheeler
public class TwoWheelerFactory implements VehicleFactory {
    public Vehicle createVehicle() {
        return new TwoWheeler();
    }
}

// Concrete factory class for FourWheeler
public class FourWheelerFactory implements VehicleFactory {
    public Vehicle createVehicle() {
        return new FourWheeler();
    }
}
```

#### Complete Code Example

```java
// Library classes
abstract class Vehicle {
    public abstract void printVehicle();
}

class TwoWheeler extends Vehicle {
    public void printVehicle() {
        System.out.println("I am two wheeler");
    }
}

class FourWheeler extends Vehicle {
    public void printVehicle() {
        System.out.println("I am four wheeler");
    }
}

// Factory Interface
interface VehicleFactory {
    Vehicle createVehicle();
}

// Concrete Factory for TwoWheeler
class TwoWheelerFactory implements VehicleFactory {
    public Vehicle createVehicle() {
        return new TwoWheeler();
    }
}

// Concrete Factory for FourWheeler
class FourWheelerFactory implements VehicleFactory {
    public Vehicle createVehicle() {
        return new FourWheeler();
    }
}

// Client class
class Client {
    private Vehicle pVehicle;

    public Client(VehicleFactory factory) {
        pVehicle = factory.createVehicle();
    }

    public Vehicle getVehicle() {
        return pVehicle;
    }
}

// Driver program
public class GFG {
    public static void main(String[] args) {
        VehicleFactory twoWheelerFactory = new TwoWheelerFactory();
        Client twoWheelerClient = new Client(twoWheelerFactory);
        Vehicle twoWheeler = twoWheelerClient.getVehicle();
        twoWheeler.printVehicle();

        VehicleFactory fourWheelerFactory = new FourWheelerFactory();
        Client fourWheelerClient = new Client(fourWheelerFactory);
        Vehicle fourWheeler = fourWheelerClient.getVehicle();
        fourWheeler.printVehicle();
    }
}
```

**Output:**
```
I am two wheeler
I am four wheeler
```

#### Explanation

- `Vehicle` serves as the Product interface, defining the common method `printVehicle()` that all concrete products must implement.
- `TwoWheeler` and `FourWheeler` are concrete product classes representing different types of vehicles, implementing the `printVehicle()` method.
- `VehicleFactory` acts as the Creator interface (Factory Interface) with a method `createVehicle()` representing the factory method.
- `TwoWheelerFactory` and `FourWheelerFactory` are concrete creator classes (Concrete Factories) implementing the `VehicleFactory` interface to create instances of specific types of vehicles.

---

## Use Cases of the Factory Method

- Used in JDBC for creating connections and in frameworks like Spring for managing beans.
- Libraries like Swing and JavaFX use factories to create flexible UI components.
- Tools like Log4j rely on factories to create configurable loggers.
- Factories help create objects from serialized data, supporting various formats.

---

## Advantages of the Factory Method

- Separates creation logic from client code, improving flexibility.
- New product types can be added easily.
- Simplifies unit testing by allowing mock product creation.
- Centralizes object creation logic across the application.
- Hides specific product classes from clients, reducing dependency.

---

## Disadvantages of the Factory Method

- Adds more classes and interfaces, which can complicate maintenance.
- Slight performance impacts due to polymorphism.
- Concrete creators are linked to their products.
- Clients need knowledge of specific subclasses.
- May lead to unnecessary complexity if applied too broadly.
- Factory logic can