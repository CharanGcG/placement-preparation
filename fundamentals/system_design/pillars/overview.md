# **Architectural Quality Attributes**

---

### 🔹 1. **Scalability**

* **Definition**: Ability of a system to handle increasing load (users, requests, data).
* **Types**:

  * **Vertical Scaling** → Add more power to a single machine (CPU, RAM).
  * **Horizontal Scaling** → Add more machines (distributed systems).

**Example:**

* Netflix scales horizontally using **microservices + AWS auto-scaling groups**.
* E-commerce apps scale during festival sales.

👉 *Design Impact*: Use load balancers, caching, database sharding.

---

### 🔹 2. **Availability**

* **Definition**: Percentage of time a system is operational (uptime).
* Often measured as **“nines”**:

  * 99% → 3.65 days downtime/year
  * 99.99% → 52 min downtime/year

**Example:**

* Banking apps aim for **99.99% availability**.
* Amazon Prime Day can’t afford outages.

👉 *Design Impact*: Use **redundancy, failover servers, health checks**.

---

### 🔹 3. **Reliability**

* **Definition**: Consistency in producing correct results without failure.
* Related to **fault tolerance**.

**Example:**

* An airline reservation system must never issue two people the same seat.
* Payment processing must either succeed **once** or not at all.

👉 *Design Impact*: Use **replication, consensus algorithms, retries**.

---

### 🔹 4. **Maintainability**

* **Definition**: Ease of fixing bugs, adding features, refactoring.
* Depends on **modularity, documentation, testability**.

**Example:**

* Microservices are more maintainable than monoliths because each service can be updated independently.
* Open-source projects with poor documentation are hard to maintain.

👉 *Design Impact*: Follow **design patterns, coding standards, CI/CD pipelines**.

---

### 🔹 5. **Performance**

* **Definition**: How fast the system responds under a given workload.
* Measured in **latency (response time)** and **throughput (requests/sec)**.

**Example:**

* Google Search aims for **<200ms response time**.
* High-frequency trading systems require **microsecond latency**.

👉 *Design Impact*: Use **caching, indexing, optimized algorithms**.

---

### 🔹 6. **Security**

* **Definition**: Protecting system against unauthorized access & attacks.

**Example:**

* Banking apps use **2FA, encryption, audit logs**.
* Social media apps need **access control + GDPR compliance**.

👉 *Design Impact*: Apply **secure design principles (least privilege, encryption, firewalls)**.

---

### 🔹 7. **Usability**

* **Definition**: How easy it is for users to interact with the system.
* Related to **UI/UX design**.

**Example:**

* Apple devices → high usability focus.
* Gov portals → often fail in usability.

👉 *Design Impact*: Consistent UI patterns, accessibility compliance.

---

### 🔹 8. **Interoperability**

* **Definition**: Ability to work with other systems.

**Example:**

* Payment gateways integrate with multiple banks.
* Healthcare apps must work with different hospital systems.

👉 *Design Impact*: Use **APIs, standard protocols, data format compatibility (JSON, XML, HL7 in healthcare)**.

---

### 🔹 9. **Testability**

* **Definition**: How easily the system can be tested.

**Example:**

* Microservices with APIs are easier to test individually.
* Monoliths often need **end-to-end testing only**.

👉 *Design Impact*: Design with **unit tests, mocks, monitoring hooks** in mind.

---

# ✅ Summary Table

| Attribute        | Key Focus                       | Example System  |
| ---------------- | ------------------------------- | --------------- |
| Scalability      | Handle more users/data          | Netflix         |
| Availability     | Minimize downtime               | Banking apps    |
| Reliability      | Correctness & fault tolerance   | Airline booking |
| Maintainability  | Easy updates/bug fixes          | Microservices   |
| Performance      | Fast response, high throughput  | Google Search   |
| Security         | Data protection, access control | Online Banking  |
| Usability        | User-friendly interface         | iPhone apps     |
| Interoperability | Works with other systems        | Payment Gateway |
| Testability      | Easy to test                    | API-driven apps |

---

✅ **Checkpoint for Students**

1. Which attribute is MOST critical for a **hospital emergency system**?
2. Which trade-off would you accept for a **social media app** — higher usability or stronger security?
3. How do scalability and availability relate but differ?

---
