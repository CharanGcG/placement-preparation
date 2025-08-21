# 1) How I’d explain it in an interview

## A) 30-second elevator pitch

“**Smart Vehicle Ignition** is a face-recognition–based ignition lock I built end-to-end. A React UI captures a live photo; the backend (Python) compares it with the registered owner’s photo (both sent as base64) and, if matched, signals an **ESP32** over serial to enable a relay that ‘unlocks’ ignition. On mismatches, it triggers a buzzer, applies a cooldown/attempt-limit, and can send alerts. Images are managed in **Google Cloud Storage**, and the system is designed to be stateless on the server for simpler scaling.”

## B) 60-90 second concise walkthrough

* **Problem & goal:** Traditional keys/FOBs are stealable. I wanted a **hands-free, owner-verified ignition** that demonstrates AI + IoT integration.
* **What I built:**

  * **Frontend (React):** Pages for Guest/Login/Register/Main. Register stores an owner photo; Main captures a live photo.
  * **Backend (Python):** Receives **two images** (registered + captured) in base64, runs face matching (encodings/embeddings), returns a verdict + message.
  * **IoT (ESP32 + Relay + Buzzer):** On success → enable relay to simulate ignition; on failure → buzzer + **cooldown/attempt-limit** to resist brute force.
  * **Cloud (GCS):** Owner images live in a bucket; frontend passes the owner image (or its URL → base64) alongside the captured one, keeping the backend **stateless** (no per-user caches).
* **Why this design:**

  * **Stateless backend** simplifies scaling and avoids local file juggling.
  * **Serial link** keeps v1 simple and transparent for debugging.
* **What it shows:** Full-stack build, hardware control, cloud storage, and security-aware features (alerts, cooldowns).

## C) 2–3 minute technical deep dive (whiteboard-friendly)

**Actors:** React client, Python API, GCS, ESP32 (relay+buzzer)

**1) Registration flow**

* User uploads a reference face on **Register** → stored in **GCS** under their user ID.
* (Current v1) When needed, the **frontend** fetches that reference (or already has it) and sends it as **base64** with each verification request—so the backend remains **stateless**.

**2) Verification (Main screen)**

* React captures a frame from the camera → base64.
* Request payload: `{ userId, registeredImageBase64, capturedImageBase64 }`.
* **Backend steps:**

  1. Decode images → face detection → face encodings.
  2. Compare embeddings (distance threshold).
  3. If **match** → write “UNLOCK” to serial → ESP32 energizes **relay** (ignition allowed).
  4. If **no match** → “ALERT” path: buzzer ON; **attempt-limit & cooldown** enforced before accepting next attempt; optional email/log.
  5. Respond to client with `{ result, message, (optional) confidence/score }`.

**3) Hardware behavior**

* **Relay** defaults to “locked.”
* On “UNLOCK,” relay enables for a safe window (e.g., N seconds) or until stop command.
* **Buzzer** warns on failed attempts.
* Cooldown is enforced **in software** to avoid spamming hardware.

**4) Why these choices**

* **React** for quick camera UX and clean state handling.
* **Python** for easy CV pipeline and serial I/O.
* **Stateless API** to keep the server simple; moving reference image via the request removes the need for backend cache/sync.
* **ESP32** for cost/efficiency; serial is the simplest reliable control path in v1.

**5) What I learned**

* Tuning face thresholds and handling edge cases (no face, multiple faces, poor lighting).
* Hardware safety (default-locked relay, explicit timeouts).
* Cloud object management and least-privilege credentials.
* Designing **for improvement**: clear seams for swapping in anti-spoofing, MQTT, or edge inference.

**Hooks for follow-ups (if they interrupt):**

* “How do you handle spoofing?” → talk liveness ideas (blink/IR/challenge-response).
* “How would you scale?” → stateless API, object storage, pre-computed embeddings, auth, and MQTT.
* “Why ESP32 over Pi?” → cost, power, boot time; Pi if you need on-device inference.

---


