Now that we’ve covered **architectural styles**, let’s go deeper into **Architectural Design Patterns**.
Think of **styles** as *city layouts* (grid, circular, distributed) and **patterns** as *building blueprints* (apartment vs. villa).

---

# **UNIT III – Architectural Design (continued)**

## **4. Architectural Design Patterns**

---

### 🔹 1. **Model–View–Controller (MVC)**

**Idea**: Separate application into 3 layers:

* **Model** – Business logic & data (DB, classes).
* **View** – UI (screens, web pages).
* **Controller** – Handles input, connects Model ↔ View.

**Example:** Web Applications (Django, Ruby on Rails, Spring MVC).

```
User → [Controller] → [Model] → [View] → User
```

**Pros:**

* Clear separation of concerns.
* Easy to maintain & test.

**Cons:**

* Can be overkill for small apps.

---

### 🔹 2. **Model–View–ViewModel (MVVM)**

**Idea**: Variation of MVC, mostly in UI-heavy apps.

* **View** → UI.
* **ViewModel** → Mediator between UI & data, uses data binding.
* **Model** → Data + business rules.

**Example:** Mobile apps (Android with Jetpack, WPF, Angular).

**Pros:**

* Great for apps with complex UIs.
* Automatic updates with data binding.

**Cons:**

* Harder to learn than MVC.

---

### 🔹 3. **Microkernel (Plug-in Architecture)**

**Idea**: Keep a **core system** with optional plug-ins.

* Core handles essential tasks.
* Plug-ins extend features dynamically.

**Example:**

* Eclipse IDE (core + plug-ins).
* Browser with extensions.

**Pros:**

* Flexible & extendable.
* Good for systems with changing requirements.

**Cons:**

* Core needs to be very stable.

---

### 🔹 4. **Event-Bus Pattern**

**Idea**: Uses a central **event bus** for communication.

* Components publish & subscribe to events.

**Example:**

* Chat apps, Notification systems, Game engines.

```
[Publisher] → [Event Bus] → [Subscribers]
```

**Pros:**

* Decoupled communication.
* Easy to add new subscribers.

**Cons:**

* Debugging event flow can be hard.

---

### 🔹 5. **Layered (n-Tier) Pattern**

**Idea**: Stack components into layers.

* Presentation, Business Logic, Data.

**Example:** University/Bank Management Systems.

**Pros:**

* Simple, well-structured.
* Easy team collaboration.

**Cons:**

* Performance overhead (too many hops).

---

### 🔹 6. **Pipes and Filters Pattern**

**Idea**: Data flows through a sequence of processing components.

* Each component (filter) transforms input → output.
* Like an **assembly line**.

**Example:**

* Compilers (Lexical Analysis → Parsing → Code Generation).
* Unix/Linux Shell Pipelines (`cat | grep | sort`).

**Pros:**

* Great for data processing.
* Highly reusable filters.

**Cons:**

* Latency if too many filters.

---

### 🔹 7. **Broker Pattern**

**Idea**: Middleware (broker) coordinates communication between clients & servers.

**Example:**

* CORBA, RMI, gRPC, Kafka (message broker).

**Pros:**

* Transparent communication.
* Good for distributed systems.

**Cons:**

* Broker is a potential bottleneck.

---

### 🔹 8. **Client–Server Pattern**

(Simpler than broker, but already discussed earlier).

**Example:** Email, Web Apps.

---

## 🔑 Summary (Patterns vs. When to Use)

* **MVC / MVVM** → Apps with UI.
* **Microkernel** → Extensible systems (IDEs, browsers).
* **Event-Bus** → Real-time apps (chat, IoT).
* **Layered** → Enterprise apps.
* **Pipes & Filters** → Data-heavy apps (compilers, ML pipelines).
* **Broker** → Distributed communication.

---

✅ **Checkpoint for Students**

1. Which pattern would you use for a **chat application** and why?
2. Why is **Pipes & Filters** ideal for building a **compiler**?
3. For a **smart home IoT system**, would you pick **Event-Bus** or **Microkernel**?

---

