# 🚀 AI-Native Knowledge System

### From static documentation → to intelligent, reasoning systems

---

## 🔥 What is this?

Most documentation systems are **passive**.
They store information—but don’t *understand* it.

This project flips that.

👉 This is an **AI-native Knowledge System** that:

* Understands user queries (even messy, multilingual input)
* Reasons across structured knowledge (KDFs)
* Returns **validated, non-hallucinated answers**

---

## ⚡ Example

**User Input:**

```text
task save ho nahi raha
```

**System Output:**

```text
Task cannot be saved

Cause:
Required fields missing or invalid

Fix Steps:
1. Fill all required fields
2. Validate input format before saving
```

👉 Input: Hindi + broken English
👉 Output: Structured, precise, actionable

---

## 🧠 Core Idea

Instead of relying only on LLMs:

```text
LLM (reasoning) + KDFs (truth) + Validator (safety)
```

This ensures:

* ❌ No hallucinations
* ✅ Deterministic outcomes
* ✅ Production reliability

---

## 🧩 Architecture

```text
User Input
   ↓
Multimodal Processor (text / voice ready)
   ↓
LLM Reasoning Layer
   ↓
KDF Retrieval (structured knowledge)
   ↓
Validation Engine (strict grounding)
   ↓
Final Answer (safe + structured)
```

---

## 🗂️ Project Structure

```text
AcmeTasker_MVP/
├── acmetasker-ui/        # Next.js frontend
├── backend/              # AI engine + APIs
├── kdf/                  # Knowledge Definition Files (truth layer)
├── requirements.txt
└── README.md
```

---

## 🧠 What are KDFs?

KDF = **Knowledge Definition File**

They define:

* Intent
* Failure scenarios
* Causes
* Resolution steps

👉 Think of them as **structured, machine-readable knowledge**

Example:

```yaml
intent:
  name: task_not_saving

failure:
  problem: Task cannot be saved

  causes:
    - id: validation_error
      label: Required fields missing or invalid

resolution:
  validation_error:
    steps:
      - Fill all required fields
      - Validate input format before saving
```

---

## 🚀 Getting Started (Local)

### 1. Clone repo

```bash
git clone https://github.com/PuneetKhamborkar/ai-native-knowledge-engine.git
cd ai-native-knowledge-engine
```

---

### 2. Backend setup

```bash
cd backend
pip install -r ../requirements.txt
python3 app.py
```

👉 Runs on: `http://127.0.0.1:5001`

---

### 3. Frontend setup

```bash
cd acmetasker-ui
npm install
npm run dev
```

👉 Open: `http://localhost:3000`

---

## 🧪 Test via API

```bash
curl -X POST http://127.0.0.1:5001/ask \
-H "Content-Type: application/json" \
-d '{"query":"task save ho nahi raha"}'
```

---

## 🌍 Features

* ✅ Multilingual input (Hindi + English mix)
* ✅ AI reasoning (LLM-based)
* ✅ Deterministic validation layer
* ✅ Structured outputs (problem → cause → fix)
* ✅ Plug-and-play knowledge via KDFs
* ⚡ Local LLM ready (Ollama support)

---

## 🎯 Why this matters

Most AI systems today:

```text
Input → LLM → Output (unreliable)
```

This system:

```text
Input → LLM → Knowledge → Validation → Trusted Output
```

👉 This is the shift from:

* AI assistants → AI systems
* chatbots → decision engines

---

## 🔮 Future Scope

* Voice input (Whisper)
* Image-based debugging
* Auto-learning KDFs
* Enterprise integrations
* Observability + feedback loops

---

## 🙌 Demo Strategy

This repo is designed for:

* 🎥 Demo videos
* 💼 Portfolio showcasing
* 🧠 System design discussions
* 🚀 AI product experimentation

---

## 👤 Author

**Puneet Khamborkar**
Building AI-native systems at the intersection of:

* Technical Writing
* Product Thinking
* Applied AI

---

## ⭐ If you found this interesting

* Star the repo
* Share your thoughts
* Let’s build smarter systems

---

## 💡 Final Thought

> Documentation tells you *what to do*
>
> AI-native systems understand *what you mean*
>
> This project is a step toward that future.
