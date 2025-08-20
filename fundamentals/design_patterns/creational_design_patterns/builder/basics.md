# Builder Design Pattern  
_Last Updated : 07 Apr, 2025_

---

The Builder Design Pattern is a creational pattern used in software design to construct a complex object step by step. It allows the construction of a product in a step-by-step manner, where the construction process can change based on the type of product being built. This pattern separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

---

## Table of Content

- Components of the Builder Design Pattern
- Steps to implement Builder Design Pattern
- Builder Design Pattern Example
- When to use Builder Design Pattern?
- When not to use Builder Design Pattern?

---

## Components of the Builder Design Pattern

1. **Product**  
   The Product is the complex object that the Builder pattern is responsible for constructing.  
   - May consist of multiple components or parts.
   - Typically a class with attributes representing the different parts that the Builder constructs.

2. **Builder**  
   The Builder is an interface or an abstract class that declares the construction steps for building a complex object.  
   - Includes methods for constructing individual parts of the product.
   - Allows for the creation of different concrete builders for product variations.

3. **ConcreteBuilder**  
   ConcreteBuilder classes implement the Builder interface, providing specific implementations for building each part of the product.  
   - Customized to create a specific variation of the product.
   - Keeps track of the product being constructed.

4. **Director**  
   The Director manages the construction process of the complex object.  
   - Collaborates with a Builder, but doesn't know the specific details about how each part is constructed.
   - Provides a high-level interface for constructing the product.

5. **Client**  
   The Client initiates the construction of the complex object.  
   - Creates a Builder object and passes it to the Director.
   - Retrieves the final product from the Builder after construction.

---

## Steps to implement Builder Design Pattern

1. **Create the Product Class:**  
   Define the object (product) that will be built. This class contains all the fields that make up the object.

2. **Create the Builder Class:**  
   This class will have methods to set the different parts of the product. Each method returns the builder itself to allow method chaining.

3. **Add a Build Method:**  
   In the builder class, add a method called `build()` (or similar) that assembles the product and returns the final object.

4. **Use the Director (Optional):**  
   You can create a director class to control the building process and decide the order in which parts are constructed.

5. **Client Uses the Builder:**  
   The client will use the builder to set the desired parts step by step and call the build() method to get the final product.

---

## Builder Design Pattern Example

**Problem Statement:**  
Implement a system for building custom computers. Each computer can have different configurations based on user preferences. The goal is to provide flexibility in creating computers with varying CPUs, RAM, and storage options.  
Use the Builder design pattern to achieve this, allowing the construction of computers through a step-by-step process.

### 1. Product (Computer)

```java
class Computer {
    private String cpu;
    private String ram;
    private String storage;

    public void setCPU(String cpu) {
        this.cpu = cpu;
    }

    public void setRAM(String ram) {
        this.ram = ram;
    }

    public void setStorage(String storage) {
        this.storage = storage;
    }

    public void displayInfo() {
        System.out.println("Computer Configuration:");
        System.out.println("CPU: " + cpu);
        System.out.println("RAM: " + ram);
        System.out.println("Storage: " + storage);
    }
}
```

### 2. Builder

```java
interface Builder {
    void buildCPU();
    void buildRAM();
    void buildStorage();
    Computer getResult();
}
```

### 3. ConcreteBuilder (GamingComputerBuilder)

```java
class GamingComputerBuilder implements Builder {
    private Computer computer;

    public GamingComputerBuilder() {
        this.computer = new Computer();
    }

    @Override
    public void buildCPU() {
        computer.setCPU("Gaming CPU");
    }

    @Override
    public void buildRAM() {
        computer.setRAM("16GB DDR4");
    }

    @Override
    public void buildStorage() {
        computer.setStorage("1TB SSD");
    }

    @Override
    public Computer getResult() {
        return computer;
    }
}
```

### 4. Director

```java
class ComputerDirector {
    public void construct(Builder builder) {
        builder.buildCPU();
        builder.buildRAM();
        builder.buildStorage();
    }
}
```

### 5. Client

```java
public class Client {
    public static void main(String[] args) {
        GamingComputerBuilder gamingBuilder = new GamingComputerBuilder();
        ComputerDirector director = new ComputerDirector();

        director.construct(gamingBuilder);
        Computer gamingComputer = gamingBuilder.getResult();

        gamingComputer.displayInfo();
    }
}
```

**Output:**
```
Computer Configuration:
CPU: Gaming CPU
RAM: 16GB DDR4
Storage: 1TB SSD
```

---

## When to use Builder Design Pattern?

- When you need to create complex objects with a large number of optional components or configuration parameters.
- When the construction of an object involves a step-by-step process where different configurations or options need to be set at different stages.
- When constructors with multiple parameters become unwieldy and error-prone.
- When you need to create objects with different configurations or variations, and want a more flexible and readable way to specify these configurations.
- When you want to provide a common interface for constructing different representations of an object.

---

## When not to use Builder Design Pattern?

- If the object you are constructing has only a few simple parameters or configurations, and the construction process is straightforward.
- In performance-critical applications, the additional overhead introduced by the Builder pattern might be a concern.
- When working with immutable objects with final fields and the object's structure is relatively simple.
- Introducing a builder class for every complex object can lead to increased code complexity.
- If the builder is tightly coupled with the product it constructs, and changes to the product require corresponding modifications to the builder, it might reduce flexibility and maintainability.
