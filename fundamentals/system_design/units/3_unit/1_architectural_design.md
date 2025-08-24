Now we’re stepping into **Unit III – Architectural Design** — this is where system design really starts to feel like *engineering a city instead of just drawing a house*.

We’ll go **deep into each architectural style**, with diagrams, pros/cons, and real-world use cases.

---

# **UNIT III – Architectural Design**

---

## **1. Introduction to Software Architecture**

* **Definition**: Software architecture is the **high-level structure** of a system, showing components and their interactions.
* Think of it as the **blueprint** for both development and deployment.
* Key goals:

  * Scalability
  * Maintainability
  * Performance
  * Security
  * Modularity

---

## **2. Common Architectural Styles**

---

### 🔹 **a) Layered Architecture (a.k.a. n-tier)**

**Idea**: Organize system into layers, each with specific responsibilities.

* **Presentation Layer** – UI (web/mobile screens).
* **Application Layer** – Business logic.
* **Data Layer** – Database handling.

**Example**: University Management System

* UI → Student Portal, Admin Dashboard
* App Logic → Enrollment, Grading, Reports
* Database → Student records, grades, courses

```
[Presentation Layer] 
       ↓
[Application Layer]
       ↓
[Data Layer]
```

**Pros:**

* Easy to understand, good separation of concerns.
* Commonly used in enterprise apps.

**Cons:**

* Can become inefficient if too many layer hops.
* Not flexible for high-performance systems.

---

### 🔹 **b) Client–Server Architecture**

**Idea**: Client requests services, server provides them.

* Client: UI, request generator.
* Server: Processes requests, manages data.

**Example**: Banking System

* Client: Mobile Banking App
* Server: Transaction Processing Server

```
[Client] ⇄ [Server]
```

**Pros:**

* Centralized control.
* Easy to manage and secure.

**Cons:**

* Server becomes bottleneck.
* Scaling is harder compared to distributed systems.

---

### 🔹 **c) Microservices Architecture**

**Idea**: Break system into **small independent services**, each responsible for one business capability.

* Services communicate via APIs (HTTP/REST, gRPC, Kafka).

**Example**: Food Delivery App

* User Service → Authentication
* Order Service → Cart & Checkout
* Payment Service → Transactions
* Delivery Service → Assigning riders

```
[User Service]   [Order Service]   [Payment Service]   [Delivery Service]
         ↘            ↘                ↘                 ↘
                [API Gateway] → Clients
```

**Pros:**

* Independent development & deployment.
* Highly scalable.
* Resilient (failure in one service doesn’t crash the whole system).

**Cons:**

* More complex (needs API gateways, service discovery).
* Harder debugging (distributed logs).

---

### 🔹 **d) Event-Driven Architecture**

**Idea**: Components communicate via **events** (publish/subscribe model).

* Instead of direct requests, services emit events that others listen to.

**Example**: E-commerce App

* Order Service publishes “Order Placed” event.
* Inventory Service listens → reduces stock.
* Payment Service listens → processes payment.
* Notification Service listens → sends SMS/email.

```
[Event Bus] ← Order Service
   ↓           ↓           ↓
Inventory   Payment   Notification
```

**Pros:**

* Decoupled services.
* Easy to add new features (just add new listeners).

**Cons:**

* Harder to guarantee data consistency.
* Debugging is tricky (who consumed what event?).

---

### 🔹 **e) Peer-to-Peer (P2P) Architecture**

**Idea**: No central server, every node acts as both client and server.

**Example**: Torrent Systems, Blockchain

```
 Node ↔ Node ↔ Node
```

**Pros:**

* Highly resilient, no single point of failure.
* Scales naturally.

**Cons:**

* Harder to secure and manage.
* Data consistency issues.

---

### 🔹 **f) Service-Oriented Architecture (SOA)**

**Idea**: Similar to microservices, but heavier and enterprise-focused.

* Uses **SOAP/XML** instead of lightweight APIs.
* Still common in large gov/finance projects.

---

## **3. Choosing the Right Architecture**

* Small University App → **Layered** (simple).
* Banking System → **Client-Server / SOA** (secure, centralized).
* Netflix, Amazon → **Microservices + Event-Driven** (scalable).
* Blockchain → **P2P** (decentralized).

---

✅ **Checkpoint for Students**

1. Which architecture would you pick for a **ride-sharing app like Uber**? Why?
2. If a system must support **real-time notifications**, which architecture (layered, event-driven, microservices) fits best?

---
