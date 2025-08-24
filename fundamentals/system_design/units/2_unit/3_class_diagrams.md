Let’s continue with **Class Diagrams**, and I’ll use **a mix of previous examples (Library, Food Delivery)** and **a new one (Banking System)** to keep things fresh.

---

# **3. UML Modeling – Class Diagrams**

### 🔹 What is a Class Diagram?

* A **structural diagram** that shows the **static view of a system**.
* Defines **classes, attributes, methods, and relationships**.
* Helps answer: *“What objects exist in the system, and how are they related?”*

---

### 🔹 Components of a Class Diagram

1. **Classes**

   * Represent entities.
   * Format:

     ```
     +-------------------+
     | Class Name        |
     +-------------------+
     | Attributes        |
     +-------------------+
     | Methods           |
     +-------------------+
     ```

2. **Relationships**

   * **Association** → “has-a” relationship.
   * **Inheritance (Generalization)** → “is-a” relationship.
   * **Aggregation** → Whole–part, weak ownership.
   * **Composition** → Strong ownership (part dies if whole dies).

---

### 🔹 Example 1: **Library Management System**

```
+-------------------+         +-------------------+
| Book              |         | Member            |
+-------------------+         +-------------------+
| bookId            |         | memberId          |
| title             |         | name              |
| author            |         | email             |
| status            |         | membershipType    |
+-------------------+         +-------------------+
| checkout()        |         | register()        |
| returnBook()      |         | borrowBook()      |
+-------------------+         +-------------------+
          |                              |
          +-----------+------------------+
                      |
               +-------------------+
               | Transaction       |
               +-------------------+
               | txnId             |
               | issueDate         |
               | returnDate        |
               | fine              |
               +-------------------+
```

**Relationships:**

* A `Member` can have many `Transaction`s.
* A `Transaction` is linked to one `Book`.

---

### 🔹 Example 2: **Food Delivery App**

```
+-------------------+         +-------------------+
| Customer          |         | Order             |
+-------------------+         +-------------------+
| custId            |         | orderId           |
| name              |         | orderStatus       |
| phone             |         | totalAmount       |
+-------------------+         +-------------------+
| placeOrder()      |         | updateStatus()    |
+-------------------+         +-------------------+
          |                              |
          +-----------+------------------+
                      |
               +-------------------+
               | Payment           |
               +-------------------+
               | paymentId         |
               | method            |
               | amount            |
               +-------------------+
               | processPayment()  |
               +-------------------+
```

---

### 🔹 Example 3: **Banking System**

```
+-------------------+         +-------------------+
| Account           |<>-------| Customer          |
+-------------------+         +-------------------+
| accountNo         |         | customerId        |
| balance           |         | name              |
| type              |         | address           |
+-------------------+         +-------------------+
| deposit()         |         | updateInfo()      |
| withdraw()        |         +-------------------+
| transfer()        |
+-------------------+
          ^
          |
+-------------------+
| SavingsAccount    |
+-------------------+
| interestRate      |
+-------------------+
| addInterest()     |
+-------------------+
```

**Relationships:**

* `Customer` owns one or more `Account`s.
* `SavingsAccount` inherits from `Account`.

---

### 🔹 Why Class Diagrams Matter

* Bridge between **requirements** and **implementation**.
* Foundation for database schema (tables often mirror classes).
* Clarify responsibilities of each module.

---

✅ **Checkpoint for Students**

* Draw a class diagram for an **Online Exam System** (Entities: Student, Exam, Question, Result).
* Which relationship would you use for:

  * **Bank Account ↔ Customer**?
  * **Exam ↔ Questions**?

---
