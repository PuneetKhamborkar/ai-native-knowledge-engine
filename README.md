AcmeTasker — AI-Native Troubleshooting System

AcmeTasker is an AI-native troubleshooting system for enterprise workflows.

It helps users diagnose and resolve operational issues such as:
- task creation failures
- visibility problems
- permission errors
- system performance issues

The system delivers precise, reliable, and non-hallucinated answers by combining structured knowledge with a controlled AI interface.

---

Core Design Principles

1. Structured Knowledge as Source of Truth (KDF)

All domain knowledge is stored in Knowledge Definition Files (KDFs).

KDFs define:
- failure scenarios
- possible causes
- resolution steps

KDFs are the single source of truth.
AI does not generate or modify this knowledge.

---

2. Controlled AI Layer (Interpretation, Not Generation)

AI is used to:
- interpret user intent
- map queries to the correct KDF
- present responses clearly

AI does NOT:
- invent causes
- generate fixes
- alter structured knowledge

---

3. Deterministic Resolution System

Once intent is identified:
- the system retrieves the exact KDF
- matches relevant causes using deterministic logic
- returns predefined resolution steps

This ensures:
- consistency
- predictability
- auditability

---

4. Separation of Responsibilities

- Knowledge → KDFs (human-curated, version-controlled)
- Matching → deterministic logic (Python)
- Language → AI (clarity, formatting, multilingual support)

This separation prevents hallucination and maintains control.

---

5. Failure-Centric Architecture

The system is designed around real-world problems.

Instead of feature-based documentation:
“How to create a task”

It focuses on:
“Why is task creation failing and how to fix it”

---

6. Multilingual Query Handling

Users can ask questions in:
- English
- mixed-language formats (e.g., Hinglish, Kannada-English)

The system:
- interprets intent using AI
- responds clearly using grounded knowledge

---

7. Human-in-the-Loop Knowledge System

KDFs are:
- authored and maintained by humans
- continuously improved
- version-controlled

AI operates strictly on top of this curated layer.

---

What Makes AcmeTasker AI-Native

Traditional systems:
- rely on AI to generate answers
- depend on static documentation

AcmeTasker:
- separates knowledge from language
- grounds every answer in structured data (KDF)
- uses AI only as an interface layer

This eliminates hallucination while preserving flexibility.

---

System Flow

User Query
   ↓
AI Intent Detection
   ↓
KDF Retrieval (source of truth)
   ↓
Deterministic Cause Matching
   ↓
Controlled AI Response (language only)

---

Outcome

- precise answers
- zero hallucination
- consistent troubleshooting
- faster issue resolution
- high trust in responses