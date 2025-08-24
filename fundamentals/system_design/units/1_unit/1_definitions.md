# **1. Definition of Systems and System Design**

### 🔹 What is a System?

A **system** is a collection of **interrelated components** working together toward a common goal by **accepting inputs, processing them, and producing outputs**.

* **Key Characteristics of a System**:

  * **Components**: Subsystems or modules (e.g., database, UI, network layer).
  * **Boundaries**: Defines what is inside the system and what interacts externally.
  * **Environment**: External entities that interact with the system (users, other systems).
  * **Input → Process → Output**: Every system has a flow of data or control.
  * **Feedback mechanism**: Used to monitor and adjust operations.

**Example (Simple System)**:

* ATM System:

  * Input: Card, PIN, transaction request.
  * Process: Authentication, balance check, withdrawal logic.
  * Output: Cash + transaction slip.

---

### 🔹 Types of Systems

1. **Physical Systems** – Hardware, machines, physical processes.
   Example: Traffic light system.
2. **Abstract Systems** – Conceptual models, software systems.
   Example: Operating system scheduler.
3. **Open Systems** – Interact with the environment.
   Example: E-commerce site with customers and suppliers.
4. **Closed Systems** – Self-contained (rare in real world).

---

### 🔹 What is System Design?

**System Design** is the **process of defining the architecture, components, modules, interfaces, and data** for a system to satisfy specified requirements.

* It answers **“How will the system work?”** after requirements are defined.
* It bridges the gap between **requirement analysis** and **system implementation**.

---

### 🔹 Levels of System Design

1. **High-Level Design (HLD)** – Defines architecture and data flow.

   * Components (e.g., authentication module, database, API).
   * Communication between modules.
   * Technology stack choices.

   *Example:* Designing a food delivery system – modules like order processing, payment, delivery tracking.

2. **Low-Level Design (LLD)** – Detailed design of each module.

   * Database schema.
   * Class diagrams.
   * API contracts.
   * Algorithms.

   *Example:* For payment module, LLD specifies card validation logic, encryption methods, database tables.

---

### 🔹 Why System Design Matters

* Ensures **scalability** (system grows with demand).
* Improves **reliability** (system is fault-tolerant).
* Reduces **development cost** by catching design flaws early.
* Provides **clarity for developers** before coding.
* Forms a **blueprint** for maintenance and upgrades.

---

✅ **Checkpoint for students:**

* **Example of a system from daily life (outside software):**  
  A **refrigerator** is a system. It consists of components like the compressor, thermostat, cooling coils, and shelves, all working together to keep food fresh. It accepts input (warm food), processes it (cools it), and produces output (cold food).

* **Difference between requirements specification and system design:**  
  - **Requirements specification** defines **what** the system should do—its functionalities, constraints, and goals (e.g., "The ATM must allow cash withdrawal and balance inquiry").
  - **System design** defines **how** the system will achieve those requirements—its architecture, components, data flow, and interfaces (e.g., "The ATM will have modules for authentication, transaction processing, and receipt printing").