Alright — let’s hit **Point 3: Current Limitations & How You Acknowledge Them.**

This is where most candidates trip — they either get **defensive** (“my project has no flaws”) or **overly negative** (“oh, it’s not good enough”).
The trick is to sound **self-aware**: you *know* where the gaps are, and you already have ideas to improve them.

---

# 3) Current Limitations (with Acknowledgement)

### 🔹 **Face Recognition Security**

* **Limitation**: Right now, the system can be fooled by a high-quality printed photo or a video on a phone. No liveness detection is present.
* **How I acknowledge**:
  “Since this was a prototype, I focused on getting basic face recognition working first. I am aware that without liveness detection, spoofing is possible, which is a major limitation for security-critical applications.”

---

### 🔹 **Scalability**

* **Limitation**: The backend compares images at runtime. If I had 1000 users, downloading reference images and re-encoding them would be slow.
* **How I acknowledge**:
  “Currently, my backend is stateless — which is good — but I send both the registered image and the captured image on each request. This is fine for a single-user demo, but at scale, it would waste bandwidth and increase latency.”

---

### 🔹 **Cloud Dependency**

* **Limitation**: Vehicle ignition requires internet access, since reference images live in Google Cloud Storage.
* **How I acknowledge**:
  “One limitation is that the system depends on cloud availability and network connectivity. In a real car, this might cause delays or failures in poor connectivity areas.”

---

### 🔹 **ESP32 Communication**

* **Limitation**: Currently uses USB serial communication. This makes it dependent on a tethered laptop/PC, which is not how real-world vehicle ECUs communicate.
* **How I acknowledge**:
  “For version 1, I chose serial because it’s simple and reliable for a demo. But I’m aware that in production, it should use secure wireless protocols like MQTT over TLS.”

---

### 🔹 **User Management**

* **Limitation**: No structured way to add/remove users. Right now, you register an image and store it in a bucket — there’s no account revocation or admin panel.
* **How I acknowledge**:
  “Currently, there’s no proper user lifecycle management. For example, I can’t easily delete or replace a user image once stored.”

---

### 🔹 **Testing & Reliability**

* **Limitation**: No automated test cases, no CI/CD, and no systematic stress-testing of the system under edge cases (multiple faces, low light, hardware failure).
* **How I acknowledge**:
  “I’ve tested it manually in controlled conditions, but it’s not battle-tested. There’s no formal test suite yet.”

---

### 🔹 **Hardware Safety**

* **Limitation**: Relay behavior depends on software commands. If the backend crashes at the wrong time, the relay could remain stuck in an “unlocked” state.
* **How I acknowledge**:
  “Right now, the system lacks hardware fail-safes. In a real ignition system, you’d want default-locked relays and watchdog timers.”

---

✨ **How it comes across in an interview**:

* Instead of *“My project is incomplete”* → you’re saying *“I know where my prototype stands, and here’s how I would improve it if I had more time/resources.”*
* That’s what impresses interviewers — they see you’re not just coding blindly, but **thinking like an engineer**.

---
