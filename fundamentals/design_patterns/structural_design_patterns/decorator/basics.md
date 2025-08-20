# Decorator Design Pattern  
_Last Updated : 23 Jul, 2025_

---

The Decorator Design Pattern is a structural design pattern that allows behavior to be added to individual objects dynamically, without affecting the behavior of other objects from the same class. It involves creating a set of decorator classes that are used to wrap concrete components.

---

## Table of Content

- What is a Decorator Design Pattern?
- Characteristics of the Decorator Pattern
- Real-World Example of Decorator Design Pattern
- Use Cases for the Decorator Pattern
- Key Components of the Decorator Design Pattern
- Example of Decorator Design Pattern
- Advantages of the Decorator Design Pattern
- Disadvantages of the Decorator Design Pattern

---

## What is a Decorator Design Pattern?

The Decorator Design Pattern is a structural design pattern used in software development. It allows behavior to be added to individual objects, dynamically, without affecting the behavior of other objects from the same class. This pattern is useful when you need to add functionality to objects in a flexible and reusable way.

---

## Characteristics of the Decorator Pattern

- Promotes flexibility and extensibility by allowing developers to compose objects with different combinations of functionalities at runtime.
- Follows the open/closed principle, as new decorators can be added without modifying existing code.
- Commonly used in scenarios where a variety of optional features or behaviors need to be added to objects in a flexible and reusable manner (e.g., text formatting, GUIs, product customization).

---

## Real-World Example of Decorator Design Pattern

Consider a video streaming platform where users can watch movies and TV shows. Each video content may have additional features or options available, such as subtitles, language preferences, video quality options, and audio enhancements.

- The base component is the video content itself.
- Decorators represent the various additional features that users can enable or customize.
- Each option acts as a decorator that enhances the viewing experience without altering the underlying video content.
- The platform can dynamically apply these additional features to the video content based on user preferences.

---

## Use Cases for the Decorator Pattern

- **Extending Functionality:** Add features or behaviors to a base component dynamically.
- **Multiple Combinations of Features:** Stack and combine decorators for customized variations.
- **Legacy Code Integration:** Extend functionality of existing objects without altering their implementation.
- **GUI Components:** Add visual effects (borders, shadows, animations) to GUI components.
- **Input/Output Streams:** Wrap streams with additional functionality (buffering, compression, encryption, logging).

---

## Key Components of the Decorator Design Pattern

- **Component Interface:** Abstract class or interface defining the common interface for both concrete components and decorators.
- **Concrete Component:** Basic objects/classes implementing the Component interface.
- **Decorator:** Abstract class implementing the Component interface and referencing a Component object.
- **Concrete Decorator:** Concrete classes extending the Decorator class, adding specific behaviors.

---

## Example of Decorator Design Pattern

**Problem Statement:**  
Build a coffee shop application where customers can order different types of coffee with optional add-ons (milk, sugar, whipped cream, etc.) using the Decorator Pattern.

### 1. Component Interface (Coffee)

```java
// Coffee.java
public interface Coffee {
    String getDescription();
    double getCost();
}
```

### 2. Concrete Component (PlainCoffee)

```java
// PlainCoffee.java
public class PlainCoffee implements Coffee {
    @Override
    public String getDescription() {
        return "Plain Coffee";
    }

    @Override
    public double getCost() {
        return 2.0;
    }
}
```

### 3. Decorator (CoffeeDecorator)

```java
// CoffeeDecorator.java
public abstract class CoffeeDecorator implements Coffee {
    protected Coffee decoratedCoffee;

    public CoffeeDecorator(Coffee decoratedCoffee) {
        this.decoratedCoffee = decoratedCoffee;
    }

    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription();
    }

    @Override
    public double getCost() {
        return decoratedCoffee.getCost();
    }
}
```

### 4. Concrete Decorators (MilkDecorator, SugarDecorator)

```java
// MilkDecorator.java
public class MilkDecorator extends CoffeeDecorator {
    public MilkDecorator(Coffee decoratedCoffee) {
        super(decoratedCoffee);
    }

    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription() + ", Milk";
    }

    @Override
    public double getCost() {
        return decoratedCoffee.getCost() + 0.5;
    }
}

// SugarDecorator.java
public class SugarDecorator extends CoffeeDecorator {
    public SugarDecorator(Coffee decoratedCoffee) {
        super(decoratedCoffee);
    }

    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription() + ", Sugar";
    }

    @Override
    public double getCost() {
        return decoratedCoffee.getCost() + 0.2;
    }
}
```

### 5. Main Class

```java
// Main.java
public class Main {
    public static void main(String[] args) {
        // Plain Coffee
        Coffee coffee = new PlainCoffee();
        System.out.println("Description: " + coffee.getDescription());
        System.out.println("Cost: $" + coffee.getCost());

        // Coffee with Milk
        Coffee milkCoffee = new MilkDecorator(new PlainCoffee());
        System.out.println("\nDescription: " + milkCoffee.getDescription());
        System.out.println("Cost: $" + milkCoffee.getCost());

        // Coffee with Sugar and Milk
        Coffee sugarMilkCoffee = new SugarDecorator(new MilkDecorator(new PlainCoffee()));
        System.out.println("\nDescription: " + sugarMilkCoffee.getDescription());
        System.out.println("Cost: $" + sugarMilkCoffee.getCost());
    }
}
```

**Output:**
```
Description: Plain Coffee
Cost: $2.0

Description: Plain Coffee, Milk
Cost: $2.5

Description: Plain Coffee, Milk, Sugar
Cost: $2.7
```

---

## Advantages of the Decorator Design Pattern

- **Open-Closed Principle:** Classes are open for extension but closed for modification.
- **Flexibility:** Add or remove responsibilities at runtime.
- **Reusable Code:** Decorators can be reused across different objects.
- **Composition over Inheritance:** Avoids deep and inflexible class hierarchies.
- **Dynamic Behavior Modification:** Apply or remove decorators at runtime.
- **Clear Code Structure:** Promotes a clear and structured design.

---

## Disadvantages of the Decorator Design Pattern

- **Complexity:** Nesting decorators can make code harder to understand and debug.
- **Increased Number of Classes:** May lead to a proliferation of small decorator classes.
- **Order of Decoration:** The order of applying decorators affects behavior.
- **Potential for Overuse:** Overusing decorators can make the codebase unnecessarily complex.
- **Limited Support in Some Languages:** Some languages may not support decorators conveniently.

---