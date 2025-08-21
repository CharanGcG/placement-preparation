# 2) Tech Stack – What I Chose, Why, and the Trade-Offs

When they ask *“Why did you pick this stack?”* the trick is to sound deliberate. Here’s how you can frame it:

---

### **Frontend – React**

* **Why I chose it**:

  * Easy camera integration (`getUserMedia`).
  * Component-driven, lets me quickly design multiple screens (Guest, Register, Login, Main).
  * Fast prototyping, widely used in the industry → keeps my portfolio relevant.
* **Trade-off**:

  * A bit heavy for just a few screens; a simpler JS/HTML app would’ve worked.
* **Future scope**:

  * Could migrate to **React Native** for mobile apps → more natural for a car setting.

---

### **Backend – Python (Flask/FastAPI)**

* **Why I chose it**:

  * Rich ecosystem → `face_recognition`, `opencv-python`.
  * Serial communication to ESP32 is straightforward (`pyserial`).
  * FastAPI in particular makes REST APIs fast to implement and easy to test.
* **Trade-off**:

  * Python isn’t the fastest for high-scale inference; latency might creep in.
* **Future scope**:

  * Could port the recognition part to a **C++/Rust library** or wrap in **ONNX/TensorRT** for speed.
  * If scaling → **containerize with Docker + deploy on GCP Cloud Run**.

---

### **Cloud – Google Cloud Storage**

* **Why I chose it**:

  * Provides reliable image storage; easy bucket integration.
  * Simple service account JSON auth.
  * I could focus on core features instead of setting up my own storage server.
* **Trade-off**:

  * Latency → pulling reference images from GCS for each attempt adds round-trip delay.
  * Security → need to handle service account carefully; credentials must not leak.
* **Future scope**:

  * Pre-compute and store embeddings (vectors) instead of raw images → reduces computation.
  * Could use **Firebase Auth + Firestore** for structured user management.

---

### **IoT Hardware – ESP32 + Relay + Buzzer**

* **Why I chose it**:

  * ESP32 is cheap, low-power, and has both WiFi + serial → good for IoT.
  * Relay module makes the ignition simulation realistic.
  * Buzzer is a simple but effective alert mechanism.
* **Trade-off**:

  * Right now, serial USB → ties me to a laptop/PC. Not production-ready.
  * ESP32 is powerful but limited for on-device face recognition.
* **Future scope**:

  * Replace serial with **MQTT over WiFi** → backend can trigger ignition remotely.
  * Move to **edge AI hardware** (e.g., ESP32-CAM, Raspberry Pi, or Coral TPU) for liveness detection and local inference.

---

### **Overall Design Choice**

* **Why this stack works for me as a student project:**

  * Balances **practicality (working prototype)** with **industry buzzwords (AI + IoT + Cloud + Web)**.
  * Shows I can **integrate multiple layers**, not just code in isolation.

* **If I had to redo for production:**

  * Swap serial → MQTT.
  * Store embeddings in DB → not images.
  * Add **JWT-based auth** for API.
  * Add **CI/CD** to auto-test and deploy.

---

👉 This way, when asked “Why React? Why Python? Why ESP32?” you won’t sound like you just randomly picked them — you’ll sound intentional, while also showing maturity by recognizing trade-offs.
