# Singleton Method Design Pattern

The Singleton Method Design Pattern ensures a class has only one instance and provides a global access point to it. It’s ideal for scenarios requiring centralized control, like managing database connections or configuration settings. This article explores its principles, benefits, drawbacks, and best use cases in software development.

---

## Table of Content

- What is Singleton Method Design Pattern?
- When to use Singleton Method Design Pattern?
- Initialization Types of Singleton
- Key Component of Singleton Method Design Pattern
- Implementation of Singleton Method Design Pattern
- Different Ways to Implement Singleton Method Design Pattern
- Use Cases for the Singleton Design Pattern
- Advantages of the Singleton Design Pattern
- Disadvantages of the Singleton Design Pattern

---

## What is Singleton Method Design Pattern?

The Singleton method or Singleton Design pattern is one of the simplest design patterns. It ensures a class only has one instance, and provides a global point of access to it.

---

## Singleton Design Pattern Principles

- **Single Instance:** Singleton ensures that only one instance of the class exists throughout the application.
- **Global Access:** Provide a global point of access to that instance.
- **Lazy or Eager Initialization:** Support creating the instance either when needed (lazy) or when the class is loaded (eager).
- **Thread Safety:** Implement mechanisms to prevent multiple threads from creating separate instances simultaneously.
- **Private Constructor:** Restrict direct instantiation by making the constructor private, forcing the use of the access point.

---

## When to use Singleton Method Design Pattern?

Use the Singleton method Design Pattern when:

- You need to ensure that only one instance of a class exists in your application.
- You want to provide a straightforward way for clients to access that instance from a specific location in your code.
- You might want to extend the class later; the Singleton pattern allows for subclassing.
- Common use cases: logging, managing connections to hardware or databases, caching data, handling thread pools.

---

## Initialization Types of Singleton

- **Early initialization:** Class is initialized whether it is to be used or not. Simple, but always initialized.
- **Lazy initialization:** Class is initialized only when required. Saves resources if not always needed.

---

## Key Component of Singleton Method Design Pattern

1. **Static Member:**  
   Ensures only one instance is created.
   ```java
   private static Singleton instance;
   ```

2. **Private Constructor:**  
   Prevents external instantiation.
   ```java
   class Singleton {
       private Singleton() {
           // Initialization code here
       }
   }
   ```

3. **Static Factory Method:**  
   Provides global access.
   ```java
   public static Singleton getInstance() {
       if (instance == null) {
           instance = new Singleton();
       }
       return instance;
   }
   ```

---

## Implementation of Singleton Method Design Pattern

```java
/*package whatever //do not write package name here */
import java.io.*;
class Singleton {
    private static Singleton instance;
    private Singleton() {
        System.out.println("Singleton is Instantiated.");
    }
    public static Singleton getInstance() {
        if (instance == null)
            instance = new Singleton();
        return instance;
    }
    public static void doSomething() {
        System.out.println("Somethong is Done.");
    }
}

class GFG {
    public static void main(String[] args) {
        Singleton.getInstance().doSomething();
    }
}
```

**Output:**
```
Singleton is Instantiated.
Somethong is Done.
```

---

## Different Ways to Implement Singleton Method Design Pattern

### Method 1 - Classic Implementation (Not Thread Safe)

```java
class Singleton {
    private static Singleton obj;
    private Singleton() {}
    public static Singleton getInstance() {
        if (obj == null)
            obj = new Singleton();
        return obj;
    }
}
```

### Method 2 - Synchronized getInstance (Thread Safe, but slower)

```java
class Singleton {
    private static Singleton obj;
    private Singleton() {}
    public static synchronized Singleton getInstance() {
        if (obj == null)
            obj = new Singleton();
        return obj;
    }
}
```

### Method 3 - Eager Instantiation (Static Initializer, Thread Safe)

```java
class Singleton {
    private static Singleton obj = new Singleton();
    private Singleton() {}
    public static Singleton getInstance() { return obj; }
}
```

### Method 4 - Double Checked Locking (Efficient & Thread Safe)

```java
class Singleton {
    private static volatile Singleton obj = null;
    private Singleton() {}
    public static Singleton getInstance() {
        if (obj == null) {
            synchronized (Singleton.class) {
                if (obj == null)
                    obj = new Singleton();
            }
        }
        return obj;
    }
}
```

### Method 5 - Inner Class (Java Specific, Thread Safe)

```java
public class Singleton {
    private Singleton() {
        System.out.println("Instance created");
    }
    private static class SingletonInner {
        private static final Singleton INSTANCE = new Singleton();
    }
    public static Singleton getInstance() {
        return SingletonInner.INSTANCE;
    }
}
```

---

## Use Cases for the Singleton Design Pattern

- Managing database connections
- Global configuration manager
- Centralized control of UI components
- Organizing print jobs in document systems

---

## Advantages of the Singleton Design Pattern

- Guarantees only one instance with a unique identifier
- Supports both eager and lazy initialization
- Can be thread-safe
- Lowers memory usage in resource-limited applications

---

## Disadvantages of the Singleton Design Pattern

- Can make unit testing difficult due to global state
- Risk of race conditions in multi-threaded environments
- Hard to refactor if multiple instances are needed later
- Creates global dependency, complicating dependency injection
- Subclassing can be tricky due to private constructor

```# Singleton Method Design Pattern

The Singleton Method Design Pattern ensures a class has only one instance and provides a global access point to it. It’s ideal for scenarios requiring centralized control, like managing database connections or configuration settings. This article explores its principles, benefits, drawbacks, and best use cases in software development.

---

## Table of Content

- What is Singleton Method Design Pattern?
- When to use Singleton Method Design Pattern?
- Initialization Types of Singleton
- Key Component of Singleton Method Design Pattern
- Implementation of Singleton Method Design Pattern
- Different Ways to Implement Singleton Method Design Pattern
- Use Cases for the Singleton Design Pattern
- Advantages of the Singleton Design Pattern
- Disadvantages of the Singleton Design Pattern

---

## What is Singleton Method Design Pattern?

The Singleton method or Singleton Design pattern is one of the simplest design patterns. It ensures a class only has one instance, and provides a global point of access to it.

---

## Singleton Design Pattern Principles

- **Single Instance:** Singleton ensures that only one instance of the class exists throughout the application.
- **Global Access:** Provide a global point of access to that instance.
- **Lazy or Eager Initialization:** Support creating the instance either when needed (lazy) or when the class is loaded (eager).
- **Thread Safety:** Implement mechanisms to prevent multiple threads from creating separate instances simultaneously.
- **Private Constructor:** Restrict direct instantiation by making the constructor private, forcing the use of the access point.

---

## When to use Singleton Method Design Pattern?

Use the Singleton method Design Pattern when:

- You need to ensure that only one instance of a class exists in your application.
- You want to provide a straightforward way for clients to access that instance from a specific location in your code.
- You might want to extend the class later; the Singleton pattern allows for subclassing.
- Common use cases: logging, managing connections to hardware or databases, caching data, handling thread pools.

---

## Initialization Types of Singleton

- **Early initialization:** Class is initialized whether it is to be used or not. Simple, but always initialized.
- **Lazy initialization:** Class is initialized only when required. Saves resources if not always needed.

---

## Key Component of Singleton Method Design Pattern

1. **Static Member:**  
   Ensures only one instance is created.
   ```java
   private static Singleton instance;
   ```

2. **Private Constructor:**  
   Prevents external instantiation.
   ```java
   class Singleton {
       private Singleton() {
           // Initialization code here
       }
   }
   ```

3. **Static Factory Method:**  
   Provides global access.
   ```java
   public static Singleton getInstance() {
       if (instance == null) {
           instance = new Singleton();
       }
       return instance;
   }
   ```

---

## Implementation of Singleton Method Design Pattern

```java
/*package whatever //do not write package name here */
import java.io.*;
class Singleton {
    private static Singleton instance;
    private Singleton() {
        System.out.println("Singleton is Instantiated.");
    }
    public static Singleton getInstance() {
        if (instance == null)
            instance = new Singleton();
        return instance;
    }
    public static void doSomething() {
        System.out.println("Somethong is Done.");
    }
}

class GFG {
    public static void main(String[] args) {
        Singleton.getInstance().doSomething();
    }
}
```

**Output:**
```
Singleton is Instantiated.
Somethong is Done.
```

---

## Different Ways to Implement Singleton Method Design Pattern

### Method 1 - Classic Implementation (Not Thread Safe)

```java
class Singleton {
    private static Singleton obj;
    private Singleton() {}
    public static Singleton getInstance() {
        if (obj == null)
            obj = new Singleton();
        return obj;
    }
}
```

### Method 2 - Synchronized getInstance (Thread Safe, but slower)

```java
class Singleton {
    private static Singleton obj;
    private Singleton() {}
    public static synchronized Singleton getInstance() {
        if (obj == null)
            obj = new Singleton();
        return obj;
    }
}
```

### Method 3 - Eager Instantiation (Static Initializer, Thread Safe)

```java
class Singleton {
    private static Singleton obj = new Singleton();
    private Singleton() {}
    public static Singleton getInstance() { return obj; }
}
```

### Method 4 - Double Checked Locking (Efficient & Thread Safe)

```java
class Singleton {
    private static volatile Singleton obj = null;
    private Singleton() {}
    public static Singleton getInstance() {
        if (obj == null) {
            synchronized (Singleton.class) {
                if (obj == null)
                    obj = new Singleton();
            }
        }
        return obj;
    }
}
```

### Method 5 - Inner Class (Java Specific, Thread Safe)

```java
public class Singleton {
    private Singleton() {
        System.out.println("Instance created");
    }
    private static class SingletonInner {
        private static final Singleton INSTANCE = new Singleton();
    }
    public static Singleton getInstance() {
        return SingletonInner.INSTANCE;
    }
}
```

---

## Use Cases for the Singleton Design Pattern

- Managing database connections
- Global configuration manager
- Centralized control of UI components
- Organizing print jobs in document systems

---

## Advantages of the Singleton Design Pattern

- Guarantees only one instance with a unique identifier
- Supports both eager and lazy initialization
- Can be thread-safe
- Lowers memory usage in resource-limited applications

---

## Disadvantages of the Singleton Design Pattern

- Can make unit testing difficult due to global state
- Risk of race conditions in multi-threaded environments
- Hard to refactor if multiple instances are needed later
- Creates global dependency, complicating dependency injection
- Subclassing can be tricky due to private constructor
