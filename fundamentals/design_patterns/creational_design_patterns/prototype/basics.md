# Prototype Design Pattern  
_Last Updated : 03 Jan, 2025_

---

The Prototype Design Pattern is a creational pattern that enables the creation of new objects by copying an existing object. Prototype allows us to hide the complexity of making new instances from the client. The existing object acts as a prototype and contains the state of the object.

---

## Table of Content

- What is Prototype Design Pattern?
- Components of Prototype Design Pattern
- Prototype Design Pattern example in Java
- When to use the Prototype Design Pattern
- When not to use the Prototype Design Pattern

---

## What is Prototype Design Pattern?

The prototype pattern is a creational design pattern which is required when object creation is a time-consuming, and costly operation, so we create objects with the existing object itself by copying the existing ones.

The newly copied object may change the same properties only if required. This approach saves costly resources and time, especially when object creation is a heavy process.

One of the best available ways to create an object from existing objects is the `clone()` method. Clone is the simplest approach to implementing a prototype pattern. However, it is your call to decide how to copy existing objects based on your business model.

Suppose a user creates a document with a specific layout, fonts, and styling, and wishes to create similar documents with slight modifications.

---

## Components of Prototype Design Pattern

- **Prototype Interface or Abstract Class:**  
  Defines the method for cloning objects and sets a standard that all concrete prototypes must follow. It includes a `clone` method that concrete prototypes will implement to create copies of themselves.

- **Concrete Prototype:**  
  Implements the prototype interface or extends the abstract class. Represents a specific type of object that can be cloned and provides the specific logic for the `clone` method.

- **Client:**  
  The code or module that requests new object creation by interacting with the prototype. It initiates the cloning process without needing to know the specifics of the concrete classes involved.

- **Clone Method:**  
  Declared in the prototype interface or abstract class and outlines how an object should be copied. Concrete prototypes implement this method to define their specific cloning behavior.

---

## Prototype Design Pattern Example in Java

Imagine you're working on a drawing application, and you need to create and manipulate various shapes. Each shape might have different attributes like color or size. Creating a new shape class for every variation becomes tedious. Also, dynamically adding or removing shapes during runtime can be challenging.

The Prototype Design Pattern helps in managing variations of shapes efficiently, promoting flexibility in shape creation, and simplifying the process of adding or removing shapes at runtime.

### 1. Prototype Interface (Shape)

```java
// This is like a blueprint for creating shapes.
// It says every shape should be able to clone itself and draw.
public interface Shape {
    Shape clone();  // Make a copy of itself
    void draw();    // Draw the shape
}
```

### 2. Concrete Prototype (Circle)

```java
// This is a specific shape, a circle, implementing the Shape interface.
// It can create a copy of itself (clone) and draw in its own way.
public class Circle implements Shape {
    private String color;

    // When you create a circle, you give it a color.
    public Circle(String color) {
        this.color = color;
    }

    // This creates a copy of the circle.
    @Override
    public Shape clone() {
        return new Circle(this.color);
    }

    // This is how a circle draws itself.
    @Override
    public void draw() {
        System.out.println("Drawing a " + color + " circle.");
    }
}
```

### 3. Client (ShapeClient)

```java
// This is like a user of shapes.
// It uses a prototype (a shape) to create new shapes.
public class ShapeClient {
    private Shape shapePrototype;

    // When you create a client, you give it a prototype (a shape).
    public ShapeClient(Shape shapePrototype) {
        this.shapePrototype = shapePrototype;
    }

    // This method creates a new shape using the prototype.
    public Shape createShape() {
        return shapePrototype.clone();
    }
}
```

### 4. Complete Code Example

```java
// Prototype interface
interface Shape {
    Shape clone();  // Make a copy of itself
    void draw();    // Draw the shape
}

// Concrete prototype
class Circle implements Shape {
    private String color;

    // When you create a circle, you give it a color.
    public Circle(String color) {
        this.color = color;
    }

    // This creates a copy of the circle.
    @Override
    public Shape clone() {
        return new Circle(this.color);
    }

    // This is how a circle draws itself.
    @Override
    public void draw() {
        System.out.println("Drawing a " + color + " circle.");
    }
}

// Client code
class ShapeClient {
    private Shape shapePrototype;

    // When you create a client, you give it a prototype (a shape).
    public ShapeClient(Shape shapePrototype) {
        this.shapePrototype = shapePrototype;
    }

    // This method creates a new shape using the prototype.
    public Shape createShape() {
        return shapePrototype.clone();
    }
}

// Main class
public class PrototypeExample {
    public static void main(String[] args) {
        // Create a concrete prototype (a red circle).
        Shape circlePrototype = new Circle("red");

        // Create a client and give it the prototype.
        ShapeClient client = new ShapeClient(circlePrototype);

        // Use the prototype to create a new shape (a red circle).
        Shape redCircle = client.createShape();

        // Draw the newly created red circle.
        redCircle.draw();
    }
}
```

**Output:**
```
Drawing a red circle.
```

---

## When to use the Prototype Design Pattern

- When creating new objects is more complex or costly than copying existing ones.
- Helpful for managing various objects with minor differences.
- Useful for dynamic configurations where you need to create objects at runtime.
- Can lower initialization costs, as cloning is often faster than building a new object from scratch.

---

## When not to use the Prototype Design Pattern

- Avoid when your application predominantly deals with unique object instances, and the overhead of implementing the pattern outweighs its benefits.
- If object creation is simple and does not involve significant resource consumption, and there are no variations of objects, using the Prototype pattern might be unnecessary complexity.
- If your objects are immutable and do not need variations, the benefits of cloning may not be significant.
- If your system has a clear and straightforward object creation process, introducing the Prototype pattern may add unnecessary complexity.