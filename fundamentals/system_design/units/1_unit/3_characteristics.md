Awesome 🚀 Let’s dive into the **third subtopic: Characteristics of Good System Design**.

This is where system design really comes alive—because these “-ilities” are what separate a **toy project** from a **production-grade system**.

---

# **3. Characteristics of Good System Design**

A good system design isn’t just about “making it work.” It’s about making it:

* **Scalable** (can handle growth),
* **Reliable** (doesn’t fail easily),
* **Available** (accessible when needed),
* **Maintainable** (easy to update and fix).

These four are often called the **pillars of quality system design**. Let’s break them down:

---

## 🔹 **1. Scalability**

* **Definition**: The ability of a system to handle increasing workload without performance degradation.
* Two types:

  * **Vertical Scaling (Scale-Up)**: Adding more power (CPU/RAM) to a single server.
  * **Horizontal Scaling (Scale-Out)**: Adding more machines/instances to distribute load.

**Techniques:**

* Load balancers.
* Database sharding and replication.
* Caching layers (e.g., Redis, CDN).

👉 **Example:**
An e-commerce site should handle **10 users today** and **10 million users on Black Friday** by scaling out servers and caching frequently viewed products.

---

## 🔹 **2. Reliability**

* **Definition**: The probability that a system performs correctly under defined conditions for a specific time.
* **Focus**: Avoiding data loss, ensuring correctness of operations.

**Techniques:**

* Redundant hardware (RAID, multiple servers).
* Database replication with failover.
* Error detection & correction mechanisms.

👉 **Example:**
When you transfer money online, the bank system **must not lose track of your money** even if a server crashes mid-transaction.

---

## 🔹 **3. Availability**

* **Definition**: The percentage of time a system is operational and accessible.
* Typically measured as **uptime (e.g., 99.9% availability = \~9 hours downtime/year)**.
* Formula:

  $$
  Availability = \frac{MTBF}{MTBF + MTTR}
  $$

  where MTBF = Mean Time Between Failures, MTTR = Mean Time To Repair.

**Techniques:**

* Redundant servers across regions.
* Automatic failover mechanisms.
* Health checks & monitoring.

👉 **Example:**
Netflix must be available **24/7 globally**. If one data center fails, another must instantly take over.

---

## 🔹 **4. Maintainability**

* **Definition**: How easy it is to **fix bugs, add features, and update** a system without breaking it.
* **Focus**: Code clarity, modularity, documentation, automation.

**Techniques:**

* Modular design (microservices).
* CI/CD pipelines for safe deployments.
* Logging & monitoring for debugging.
* Proper API versioning.

👉 **Example:**
If Amazon wants to add a **“Buy Now Pay Later”** feature, the system should allow this without rewriting the entire checkout flow.

---

### ⚖️ **Trade-offs**

* Sometimes, improving one characteristic may weaken another:

  * Adding **replication** improves availability but may reduce consistency.
  * Designing for extreme scalability may make maintainability harder.

This is where **architectural decisions** and **design trade-offs** come in (later covered under CAP theorem, PACELC, etc.).

---

### 🔹 **Analogy**

Think of designing a **hospital**:

* **Scalable** → Can add more wards when patients increase.
* **Reliable** → Equipment works correctly.
* **Available** → Emergency services open 24/7.
* **Maintainable** → Easy to upgrade medical equipment without shutting the hospital down.

---

✅ **Checkpoint for students:**

### 1. High Reliability but Low Availability: What Does It Mean?

- **High reliability** means the system rarely fails or produces errors; it performs its intended function consistently when it is running.
- **Low availability** means the system is not accessible or operational for much of the time—it may be down, offline, or under maintenance for long periods.

> **In simple terms:**  
> The system works very well when it’s up, but it’s rarely up or accessible.

**Example:**  
- A legacy internal business tool that’s robust and bug-free, but is only accessible during a few working hours each week, or is often down due to scheduled maintenance or infrastructure limitations.
- Old backup servers that work flawlessly (high reliability), but are only powered on during monthly backup cycles (low availability).

***

### 2. Real-World App That Prioritizes Scalability Over Reliability

- **Scalability over reliability** means the app is designed to handle a huge number of users or transactions, even if that sometimes leads to occasional glitches, delays, or temporary service drops.

**Common Example:**  
- **Social media platforms (e.g., Twitter/X, Instagram):**  
  These services prioritize scaling up rapidly for surges in user activity (like viral events or hashtag campaigns) and massive concurrent access.  
  Sometimes, users experience temporary outages ("fail whales" on Twitter, Instagram loading issues) because the focus is on serving as many users as possible, even if reliability takes a hit occasionally.

- **Food delivery apps during festivals/peak hours (e.g., Swiggy, Zomato):**  
  The apps sometimes crash or get sluggish when everyone is ordering at once, but their architecture is designed to try and accommodate scale first.

***

#### Interview-Friendly Table

| Concept                         | Key Point                                                                 | Example App         | Copy-paste for revision |
|----------------------------------|--------------------------------------------------------------------------|---------------------|------------------------|
| High reliability, low availability | System works well when running, but is rarely accessible                  | Legacy backup server | "Runs perfectly when up, but rarely up" |
| Scalability over reliability     | Handles more users at the cost of occasional errors or downtime           | Instagram, Swiggy   | "Scales fast, but sometimes fails"     |

***

**Tip:**  
Think of platforms that grow rapidly or must handle unpredictable spikes—they know reliability might occasionally dip, but user reach and scale come first.