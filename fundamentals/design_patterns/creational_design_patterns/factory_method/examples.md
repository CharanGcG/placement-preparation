## 🔑 **Clear Explanation**

The **problem**:
If the client creates objects directly using `new`, then whenever a new subclass is introduced (say, a new type of coffee), the **client code needs to change** everywhere. This violates the **Open/Closed Principle** (code should be open for extension but closed for modification).

The **solution (Factory Method Pattern)**:

* Define a **factory interface/abstract class** with a method like `createCoffee()`.
* Let **subclasses** of the factory decide which coffee to create.
* The **client only depends on the factory interface**, not the concrete coffee classes.

This way, new coffee types can be added without modifying the client.

---

## ☕ Coffee Machine Example in Java

```java
// Product interface
interface Coffee {
    void prepare();
}

// Concrete Products
class Espresso implements Coffee {
    public void prepare() {
        System.out.println("Preparing Espresso Coffee ☕");
    }
}

class Cappuccino implements Coffee {
    public void prepare() {
        System.out.println("Preparing Cappuccino Coffee ☕");
    }
}

// Factory (Creator)
abstract class CoffeeFactory {
    // Factory Method
    abstract Coffee createCoffee();
}

// Concrete Factories
class EspressoFactory extends CoffeeFactory {
    public Coffee createCoffee() {
        return new Espresso();
    }
}

class CappuccinoFactory extends CoffeeFactory {
    public Coffee createCoffee() {
        return new Cappuccino();
    }
}

// Factory Provider (hides selection logic)
class CoffeeFactoryProvider {
    public static CoffeeFactory getFactory(String type) {
        switch (type.toLowerCase()) {
            case "espresso": return new EspressoFactory();
            case "cappuccino": return new CappuccinoFactory();
            default: throw new IllegalArgumentException("Unknown coffee type: " + type);
        }
    }
}

// Client
public class CoffeeMachine {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter coffee type (espresso/cappuccino): ");
        String type = scanner.nextLine();

        // Client doesn’t change if we add new coffee types
        CoffeeFactory factory = CoffeeFactoryProvider.getFactory(type);
        Coffee coffee = factory.createCoffee();
        coffee.prepare();
    }
}
```

---

## 📝 Key Takeaways

1. **Base class (interface)** → `Coffee`.
2. **Subclasses** → `Espresso`, `Cappuccino`.
3. **Factory interface/abstract class** → `CoffeeFactory`.
4. **Concrete Factories** → `EspressoFactory`, `CappuccinoFactory`.
5. **Client** (`CoffeeMachine`) → asks the factory to create coffee, doesn’t `new` anything directly.

---

## 🎯 Why This Works

* **Extensible**: Adding a new type (say `Latte`) requires only a new subclass + factory, no changes in client.
* **Runtime decision**: The factory used (`EspressoFactory` or `CappuccinoFactory`) can be chosen at runtime.
* **Loose coupling**: Client depends only on the `Coffee` interface, not concrete classes.

---

