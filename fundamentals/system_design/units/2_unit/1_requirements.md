Let’s roll into **Unit II – Requirements and Modeling** with the **first subtopic: Requirements Analysis (Functional vs. Non-Functional Requirements).**

---

# **Unit II – Requirements and Modeling**

## **1. Requirements Analysis**

Before designing or coding a system, we must know **what the system is supposed to do**. This is called **requirements analysis**.

### 🔹 What are Requirements?

* **Requirements** are statements that describe the **features, behavior, and constraints** of a system.
* They act as the **contract** between stakeholders (customers, users) and developers.

---

### 🔹 Types of Requirements

#### 1. **Functional Requirements (FRs)**

* Define **what the system should do**.
* Describe the **features, functions, and services**.
* Usually expressed as **use cases** or **user stories**.

**Examples:**

* A Library System must allow members to **search books by title or author**.
* An E-commerce app must let users **add items to cart** and **make payments**.
* A Banking System must allow **fund transfer between accounts**.

👉 Think: *Functions that the system performs.*

---

#### 2. **Non-Functional Requirements (NFRs)**

* Define **how the system should perform**.
* Constraints or quality attributes (performance, security, reliability, usability).
* Often described with “-ilities.”

**Examples:**

* The system should support **1000 concurrent users** (scalability).
* System availability must be **99.99% uptime** (availability).
* Payment data must be **encrypted** (security).
* Page load time must be **< 2 seconds** (performance).

👉 Think: *Conditions under which the system operates.*

---

### 🔹 Differences Between FRs and NFRs

| Aspect          | **Functional Requirements (FRs)**   | **Non-Functional Requirements (NFRs)**    |
| --------------- | ----------------------------------- | ----------------------------------------- |
| **Focus**       | What the system does                | How the system works                      |
| **Type**        | Features, use cases, services       | Performance, scalability, usability       |
| **Measurable?** | Yes, directly testable              | Often needs metrics (e.g., response < 1s) |
| **Example**     | “User can reset password via email” | “Password reset must complete within 10s” |

---

### 🔹 Requirement Gathering Techniques

1. **Interviews** – Talking with stakeholders.
2. **Questionnaires** – For large groups.
3. **Observation** – Watching users interact with current system.
4. **Workshops / Brainstorming** – Group sessions.
5. **Prototyping** – Early mockups for feedback.

---

### 🔹 Why Requirement Analysis is Critical

* Prevents **scope creep** (adding features later without planning).
* Reduces **cost of rework** (fixing wrong assumptions later is expensive).
* Provides a **clear roadmap** for design and testing.

---

✅ **Checkpoint for Students**

* Can you think of **two FRs** and **two NFRs** for a **food delivery app**?
* Why might NFRs be harder to test than FRs?

### ✅ Checkpoint Answers

***

#### 1. Two Functional Requirements (FRs) for a Food Delivery App

- **Order Placement:** Customers must be able to browse menus, select items, and place an order with payment options.
- **Real-Time Delivery Tracking:** Users should be able to see the live location of their delivery person until the order arrives.

***

#### 2. Two Non-Functional Requirements (NFRs) for a Food Delivery App

- **Scalability:** The app should handle a sudden increase in simultaneous users during peak hours without performance degradation.
- **Availability:** The service should remain accessible 24/7 with minimal downtime, ensuring users can order anytime.

***

#### 3. Why NFRs are Harder to Test than FRs

- **NFRs are often qualitative and system-wide:** Unlike FRs that specify concrete actions, NFRs deal with qualities like performance, reliability, or usability, which are harder to measure with simple test cases.
- **Testing requires complex environments and load:** For example, testing scalability or availability needs simulations of high load, varied network conditions, and long uptime periods, which are resource-intensive and technically challenging.
- **NFRs involve multiple system components:** Their impact is often cross-cutting and depends on the interaction of many modules, making pinpointing issues more complex.
- **Observable only indirectly:** You can't usually "check off" an NFR the same way as a feature; it needs monitoring, metrics, or user feedback to evaluate effectively.

***

This distinction emphasizes why thorough planning and specialized testing approaches are essential for NFRs in system design.