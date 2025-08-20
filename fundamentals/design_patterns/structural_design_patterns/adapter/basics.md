# Adapter Design Pattern

---

The **Adapter Pattern** is a **structural design pattern** that allows objects with incompatible interfaces to work together. It acts as a bridge between the client (which expects a specific interface) and an existing class (Adaptee) with a different interface.

---

## Table of Content

- What is Adapter Design Pattern?
- When to use Adapter Design Pattern?
- Types of Adapter Pattern
- Components of Adapter Design Pattern
- Adapter Pattern Example (Mobile Charger)
- Advantages of Adapter Design Pattern
- Disadvantages of Adapter Design Pattern

---

## What is Adapter Design Pattern?

The Adapter Pattern enables two incompatible interfaces to work together. It wraps an existing class (Adaptee) with an Adapter that implements the expected interface (Target), translating calls so the client can use the Adaptee seamlessly.

---

## When to use Adapter Design Pattern?

- When you want to use an existing class, but its interface does not match what the client expects.
- When integrating legacy code or third-party libraries into your system.
- When you need to bridge between different APIs or systems.

---

## Types of Adapter Pattern

- **Class Adapter:** Uses inheritance to adapt one interface to another.
- **Object Adapter:** Uses composition (recommended) to adapt one interface to another.

---

## Components of Adapter Design Pattern

- **Target Interface:** The interface expected by the client.
- **Adaptee:** The existing class with an incompatible interface.
- **Adapter:** The bridge that implements the Target interface and translates calls to the Adaptee.
- **Client:** The code that uses the Target interface.

---

## Adapter Pattern Example (Mobile Charger)

### 1. Target Interface

```java
// Target interface
interface MobileCharger {
    void chargeMobile();
}
```

### 2. Adaptee (Incompatible Class)

```java
// Adaptee class (incompatible)
class ElectricSocket {
    public void supplyPower() {
        System.out.println("Supplying 220V power...");
    }
}
```

### 3. Adapter (Object Adapter)

```java
// Adapter class
class ChargerAdapter implements MobileCharger {
    private ElectricSocket socket;

    public ChargerAdapter(ElectricSocket socket) {
        this.socket = socket;
    }

    @Override
    public void chargeMobile() {
        socket.supplyPower();
        System.out.println("Adapter converts 220V → 5V");
        System.out.println("Mobile is charging safely at 5V!");
    }
}
```

### 4. Client Code

```java
public class AdapterPatternDemo {
    public static void main(String[] args) {
        // Client expects MobileCharger
        ElectricSocket socket = new ElectricSocket();
        MobileCharger charger = new ChargerAdapter(socket);

        // Now the client can use incompatible class
        charger.chargeMobile();
    }
}
```

### Output

```
Supplying 220V power...
Adapter converts 220V → 5V
Mobile is charging safely at 5V!
```

---

## Advantages of Adapter Design Pattern

- Promotes code reusability by allowing integration of existing classes.
- Supports legacy code and third-party libraries.
- Decouples client code from implementation details of Adaptee.

---

## Disadvantages of Adapter Design Pattern

- May add extra complexity to the codebase.
- Too many adapters can make the system harder to maintain.
- Adapter may not work if Adaptee has incompatible behavior beyond interface mismatch.

---

## Key Points for Interviews

- Use Adapter when you need to integrate incompatible interfaces.
- Prefer **Object Adapter** (composition) over **Class Adapter** (inheritance).
- Real-world analogy: A travel adapter for charging your phone abroad.

---