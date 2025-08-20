# Bridge Design Pattern

---

The **Bridge Pattern** is a **structural design pattern** used to **decouple abstraction from implementation**, allowing both to vary independently. It solves the class explosion problem by favoring composition over inheritance.

---

## Table of Content

- What is Bridge Design Pattern?
- Why use Bridge Design Pattern?
- Components of Bridge Design Pattern
- Bridge Design Pattern Example (Shapes & Colors)
- Advantages of Bridge Design Pattern
- Disadvantages of Bridge Design Pattern
- Real-world Analogies

---

## What is Bridge Design Pattern?

The Bridge Pattern separates the abstraction (high-level logic) from its implementation (low-level details) so that both can be developed and extended independently.

---

## Why use Bridge Design Pattern?

- Avoids class explosion when combining multiple abstractions and implementations.
- Promotes flexibility and scalability.
- Enables independent evolution of abstraction and implementation.

---

## Components of Bridge Design Pattern

- **Abstraction:** High-level interface (e.g., `Shape`).
- **Implementor:** Low-level interface (e.g., `Color`).
- **Refined Abstraction:** Concrete abstraction (e.g., `Circle`, `Square`).
- **Concrete Implementor:** Concrete implementation (e.g., `RedColor`, `GreenColor`).
- **Bridge:** Composition relationship between Abstraction and Implementor.
- **Client:** Uses the abstraction.

---

## Bridge Design Pattern Example (Drawing Shapes with Colors)

### 1. Implementor (Bridge Interface)

```java
// Implementor interface
interface Color {
    void applyColor();
}
```

### 2. Concrete Implementors

```java
class RedColor implements Color {
    public void applyColor() {
        System.out.println("Applying red color");
    }
}

class GreenColor implements Color {
    public void applyColor() {
        System.out.println("Applying green color");
    }
}
```

### 3. Abstraction

```java
abstract class Shape {
    // Bridge: has-a relationship with Color
    protected Color color;

    public Shape(Color color) {
        this.color = color;
    }

    abstract void draw();
}
```

### 4. Refined Abstraction

```java
class Circle extends Shape {
    public Circle(Color color) {
        super(color);
    }

    @Override
    void draw() {
        System.out.print("Drawing Circle → ");
        color.applyColor();
    }
}

class Square extends Shape {
    public Square(Color color) {
        super(color);
    }

    @Override
    void draw() {
        System.out.print("Drawing Square → ");
        color.applyColor();
    }
}
```

### 5. Client Code

```java
public class BridgePatternDemo {
    public static void main(String[] args) {
        Shape redCircle = new Circle(new RedColor());
        Shape greenSquare = new Square(new GreenColor());

        redCircle.draw();
        greenSquare.draw();
    }
}
```

### Output

```
Drawing Circle → Applying red color
Drawing Square → Applying green color
```

---

## Advantages of Bridge Design Pattern

- Decouples abstraction from implementation.
- Avoids class explosion.
- Supports open/closed principle for both abstraction and implementation.
- Enables independent extension of abstraction and implementation.

---

## Disadvantages of Bridge Design Pattern

- Adds complexity with more classes and interfaces.
- May be overkill for simple scenarios.

---

## Real-world Analogies

- **Remote control (Abstraction)** ↔ **TV (Implementor)**: Different remotes and TVs can evolve independently.
- **UI Themes**: Components (Button, TextField) use themes (Dark, Light) without rewriting every component for each theme.

---
```# Bridge Design Pattern

---

The **Bridge Pattern** is a **structural design pattern** used to **decouple abstraction from implementation**, allowing both to vary independently. It solves the class explosion problem by favoring composition over inheritance.

---

## Table of Content

- What is Bridge Design Pattern?
- Why use Bridge Design Pattern?
- Components of Bridge Design Pattern
- Bridge Design Pattern Example (Shapes & Colors)
- Advantages of Bridge Design Pattern
- Disadvantages of Bridge Design Pattern
- Real-world Analogies

---

## What is Bridge Design Pattern?

The Bridge Pattern separates the abstraction (high-level logic) from its implementation (low-level details) so that both can be developed and extended independently.

---

## Why use Bridge Design Pattern?

- Avoids class explosion when combining multiple abstractions and implementations.
- Promotes flexibility and scalability.
- Enables independent evolution of abstraction and implementation.

---

## Components of Bridge Design Pattern

- **Abstraction:** High-level interface (e.g., `Shape`).
- **Implementor:** Low-level interface (e.g., `Color`).
- **Refined Abstraction:** Concrete abstraction (e.g., `Circle`, `Square`).
- **Concrete Implementor:** Concrete implementation (e.g., `RedColor`, `GreenColor`).
- **Bridge:** Composition relationship between Abstraction and Implementor.
- **Client:** Uses the abstraction.

---

## Bridge Design Pattern Example (Drawing Shapes with Colors)

### 1. Implementor (Bridge Interface)

```java
// Implementor interface
interface Color {
    void applyColor();
}
```

### 2. Concrete Implementors

```java
class RedColor implements Color {
    public void applyColor() {
        System.out.println("Applying red color");
    }
}

class GreenColor implements Color {
    public void applyColor() {
        System.out.println("Applying green color");
    }
}
```

### 3. Abstraction

```java
abstract class Shape {
    // Bridge: has-a relationship with Color
    protected Color color;

    public Shape(Color color) {
        this.color = color;
    }

    abstract void draw();
}
```

### 4. Refined Abstraction

```java
class Circle extends Shape {
    public Circle(Color color) {
        super(color);
    }

    @Override
    void draw() {
        System.out.print("Drawing Circle → ");
        color.applyColor();
    }
}

class Square extends Shape {
    public Square(Color color) {
        super(color);
    }

    @Override
    void draw() {
        System.out.print("Drawing Square → ");
        color.applyColor();
    }
}
```

### 5. Client Code

```java
public class BridgePatternDemo {
    public static void main(String[] args) {
        Shape redCircle = new Circle(new RedColor());
        Shape greenSquare = new Square(new GreenColor());

        redCircle.draw();
        greenSquare.draw();
    }
}
```

### Output

```
Drawing Circle → Applying red color
Drawing Square → Applying green color
```

---

## Advantages of Bridge Design Pattern

- Decouples abstraction from implementation.
- Avoids class explosion.
- Supports open/closed principle for both abstraction and implementation.
- Enables independent extension of abstraction and implementation.

---

## Disadvantages of Bridge Design Pattern

- Adds complexity with more classes and interfaces.
- May be overkill for simple scenarios.

---

## Real-world Analogies

- **Remote control (Abstraction)** ↔ **TV (Implementor)**: Different remotes and TVs can evolve independently.
- **UI Themes**: Components (Button, TextField) use themes (Dark, Light) without rewriting every component for each theme.

---