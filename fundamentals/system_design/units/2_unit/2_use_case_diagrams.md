Let’s start **Modeling with UML** – the most widely used way to visualize requirements and system design.

We’ll go **step by step** through the key UML diagrams, beginning with **Use Case Diagrams**.

---

# **2. UML Modeling – Use Case Diagrams**

### 🔹 What is a Use Case Diagram?

* A **visual representation** of the system’s **functional requirements**.
* Shows the **interactions between actors (users/external systems)** and the **system’s use cases (functionalities)**.
* Helps answer: *“Who uses the system, and what can they do with it?”*

---

### 🔹 Components of a Use Case Diagram

1. **Actors** – External entities that interact with the system.

   * Human users (Student, Admin, Customer).
   * External systems (Payment Gateway, Email Service).

2. **Use Cases** – Functionalities provided by the system (Enroll in Course, Issue Book, Make Payment).

3. **System Boundary** – A box showing what’s inside (system responsibilities) vs. outside (actors).

4. **Relationships** – Connections between actors and use cases.

   * **Association** (straight line: actor ↔ use case).
   * **Include** (reusable functionality).
   * **Extend** (optional/conditional functionality).

---

### 🔹 Example: **Library Management System (LMS)**

**Actors**: Student, Librarian
**Use Cases**: Search Book, Borrow Book, Return Book, Pay Fine, Manage Books

**Textual Diagram Representation (since I can’t draw here):**

```
[Student] --------> (Search Book)
[Student] --------> (Borrow Book)
[Student] --------> (Return Book)
[Student] --------> (Pay Fine)

[Librarian] ------> (Manage Books)
[Librarian] ------> (Manage Students)
```

---

### 🔹 Example: **Food Delivery App**

**Actors**: Customer, Delivery Partner, Restaurant, Payment Gateway
**Use Cases**: Browse Menu, Place Order, Track Delivery, Make Payment, Update Order Status

```
[Customer] ----------> (Browse Menu)
[Customer] ----------> (Place Order) ----> <<include>> (Make Payment)
[Customer] ----------> (Track Delivery)

[Delivery Partner] --> (Update Order Status)
[Restaurant] --------> (Update Menu)
[Payment Gateway] ---> (Process Payment)
```

---

### 🔹 Why Use Case Diagrams?

* Simple & intuitive for non-technical stakeholders.
* Captures **functional requirements clearly**.
* Forms the base for deeper modeling (sequence, class diagrams).

---

✅ **Checkpoint for Students**

* Draw a simple **use case diagram for an Online Exam System**. (Actors: Student, Instructor, Admin; Use Cases: Take Exam, Evaluate Exam, Add Questions, Generate Results).

---
