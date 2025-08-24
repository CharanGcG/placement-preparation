Let’s continue into **Sequence Diagrams**.
This is where we move from *static structure (class diagrams)* → *dynamic behavior (time-ordered interactions)*.

---

# **4. UML Modeling – Sequence Diagrams**

### 🔹 What is a Sequence Diagram?

* A **behavioral UML diagram** that shows **how objects interact in a particular scenario**.
* Focuses on **time sequence of messages**.
* Helps answer: *“How do system components talk to each other step by step?”*

---

### 🔹 Components of a Sequence Diagram

1. **Actors/Objects** → Shown as vertical lifelines.
   (e.g., `Customer`, `System`, `Payment Gateway`).
2. **Messages** → Arrows between lifelines representing method calls/data flow.

   * Solid arrow: synchronous call.
   * Dashed arrow: return message.
3. **Activation Bar** → Shows when an object is active/processing.
4. **Lifeline** → Vertical dashed line representing the existence of an object over time.

---

### 🔹 Example 1: **Library Management – Borrow Book**

Actors: `Member`, `Library System`, `Book Database`

**Flow:**

1. Member requests to borrow book.
2. System checks availability in DB.
3. If available → Issue book & update record.
4. System returns confirmation to Member.

```
Member  → LibrarySystem : borrowBook(bookId)
LibrarySystem → BookDB  : checkAvailability(bookId)
BookDB → LibrarySystem  : available
LibrarySystem → BookDB  : updateRecord(memberId, bookId)
LibrarySystem → Member  : confirmBorrow(success)
```

---

### 🔹 Example 2: **Food Delivery App – Place Order & Payment**

Actors: `Customer`, `Order Service`, `Payment Gateway`, `Restaurant`, `Delivery Service`

**Flow:**

1. Customer places order.
2. Order Service creates order.
3. Payment processed via Payment Gateway.
4. Restaurant gets order.
5. Delivery Service assigns rider.
6. Customer gets confirmation.

```
Customer → OrderService : placeOrder(items)
OrderService → PaymentGateway : processPayment(details)
PaymentGateway → OrderService : paymentSuccess
OrderService → Restaurant : newOrder(orderId)
Restaurant → OrderService : orderAccepted
OrderService → DeliveryService : assignRider(orderId)
DeliveryService → OrderService : riderAssigned
OrderService → Customer : confirmOrder(orderId, ETA)
```

---

### 🔹 Example 3: **Banking System – Fund Transfer**

Actors: `Customer`, `Banking App`, `Account Service`, `Transaction DB`, `Notification Service`

**Flow:**

1. Customer requests transfer.
2. App verifies account balance.
3. Transaction recorded in DB.
4. Balance updated for sender and receiver.
5. Confirmation + SMS/Email sent.

```
Customer → BankingApp : transferFunds(sender, receiver, amount)
BankingApp → AccountService : checkBalance(sender)
AccountService → BankingApp : balanceOK
BankingApp → TransactionDB : createTransaction(txnId, amount)
TransactionDB → BankingApp : transactionSaved
BankingApp → AccountService : updateBalances()
AccountService → BankingApp : balancesUpdated
BankingApp → NotificationService : sendConfirmation()
NotificationService → Customer : SMS/Email Confirmation
```

---

### 🔹 Why Sequence Diagrams Matter

* Clarify **order of operations** (esp. in distributed systems).
* Useful for **debugging workflows** (e.g., why payment fails).
* Ensures **all actors are accounted for**.
* Forms a base for **API design & integration testing**.

---

✅ **Checkpoint for Students**

* Draw a sequence diagram for **Online Exam Submission**:

  * Actors: Student, Exam Portal, Grading Service, Result DB.
  * Flow: Student submits → Portal saves → Grading service evaluates → Result stored → Confirmation shown.

---
