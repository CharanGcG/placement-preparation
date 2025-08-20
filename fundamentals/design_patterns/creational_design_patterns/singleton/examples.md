The **Singleton Pattern** ensures that a class has only **one instance** in the entire application, and provides a **global access point** to that instance.

Here are different ways to implement it in **Java**:

---

### ✅ 1. **Eager Initialization (simple, thread-safe)**

```java
class Singleton {
    // instance created at class loading
    private static final Singleton instance = new Singleton();

    // private constructor prevents instantiation
    private Singleton() {}

    // global access point
    public static Singleton getInstance() {
        return instance;
    }
}
```

* Pros: Thread-safe, simple
* Cons: Instance is created even if it’s never used

---

### ✅ 2. **Lazy Initialization (not thread-safe)**

```java
class Singleton {
    private static Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton(); // created only when needed
        }
        return instance;
    }
}
```

* Pros: Instance created only when needed
* Cons: **Not thread-safe** (multiple threads may create multiple instances)

---

### ✅ 3. **Thread-Safe with `synchronized`**

```java
class Singleton {
    private static Singleton instance;

    private Singleton() {}

    public static synchronized Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```

* Pros: Safe in multi-threaded environment
* Cons: Synchronization makes it **slower**

---

### ✅ 4. **Double-Checked Locking (best practice)**

```java
class Singleton {
    private static volatile Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) { // first check
            synchronized (Singleton.class) {
                if (instance == null) { // second check
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```

* Pros: Thread-safe, efficient
* Cons: A bit more complex

---

### ✅ 5. **Bill Pugh Solution (Inner Static Helper Class)**

```java
class Singleton {
    private Singleton() {}

    // inner static class holds the instance
    private static class SingletonHelper {
        private static final Singleton INSTANCE = new Singleton();
    }

    public static Singleton getInstance() {
        return SingletonHelper.INSTANCE;
    }
}
```

* Pros: **Best approach** – thread-safe, lazy-loaded, no synchronization overhead

---

### ✅ 6. **Enum Singleton (simplest + serialization safe)**

```java
enum Singleton {
    INSTANCE;

    public void doSomething() {
        System.out.println("Singleton using Enum");
    }
}
```

* Pros: Thread-safe, prevents reflection attacks, serialization-safe
* Cons: Can’t extend other classes

---

👉 In **interviews**, usually the **Bill Pugh approach** or **Double-Checked Locking** is expected, since they combine **lazy initialization** with **thread safety**.

---
