# Lesson Plan: Architecting Trustworthy Local AI Systems
**Course: Advanced Generative AI & Retrieval Systems**
**Instructor:** [Your Name]
**Institution:** Indian Institute of Technology (IIT) - Teaching Demo
**Theme:** *From Black-Box APIs to Local Mastery: The 2026 Shift*

---

## 🎓 1. Learning Objectives (LOs)
By the end of this session, participants will be able to:
1. **Deconstruct** the RAG (Retrieval-Augmented Generation) pipeline: Load, Split, Embed, Store, and Retrieve.
2. **Evaluate** the benefits of Local Inference (Ollama/LangChain) over Cloud APIs (Privacy, Cost, Latency).
3. **Analyze** Multimodal interaction paradigms using Vision-Language Models (VLM).
4. **Implement** Persona-Driven Engineering for educational agents using centralized configuration.

---

## ⚡ 2. The Hook: The "Privacy-Paradox" (5 mins)
*   **Discussion Starter:** "If we build high-intelligence agents on cloud APIs, are we building products or just renting brains?"
*   **The Proposition:** Today, we demonstrate how to build a sovereign AI stack that runs entirely on-premise, using the same "Silicon Valley Standards" but with zero data leakage.

---

## 🛠 3. Technical Module 1: Anatomy of a Modern Local Stack (10 mins)
*   **The Engine:** Ollama (Local Model Hosting)
*   **The Orchestrator:** LangChain (Managing the "Thought Loop")
*   **The Persona:** Caramel AI (The "ELI10" Framework)
    *   *Concept:* Why a 10-year-old persona is the gold standard for pedagogical clarity.
    *   *Code Insight:* Show the `config.SYSTEM_PROMPT` centralization in `config.py`.

---

## 📂 4. Module 2: Retrieval-Augmented Generation (RAG) (15 mins)
*   **The Problem:** LLM Hallucination & Knowledge Cut-offs.
*   **The Solution:** Grounding the model in current reality.
*   **Live Case Studies (Selected from the Project):**
    *   **Text RAG (Project 3):** Simulating institutional memory.
    *   **Web RAG (Project 4):** Real-time situational awareness (Crawling `ruthranraghavan.com`).
    *   **Vector RAG (Project 7):** Explain FAISS and Semantic Search. *Why use Vector DBs over Keyword Search?*

---

## 👁 5. Module 3: Multimodality & Vision-Language Models (10 mins)
*   **Beyond Text:** Integrating `qwen3-vl`.
*   **Demo:** Project 8 (AI Image Describer).
    *   *Key Takeaway:* How Base64 encoding bridges the gap between raw binary images and LLM tokens.

---

## 🏗 6. Architectural Walkthrough: "The Clean Code Ethos" (10 mins)
*   **Project 1 vs. Project 2:** Transitioning from Stateless to Stateful (Memory Management).
*   **Modular Design:** Explain the `sys.path` injection and absolute path resolution used in the workspace.
    *   *Pedagogical Point:* "Scalability starts with a single configuration file (`config.py`)."

---

## 🧪 7. Demo Strategy (The "Grand Finale")
1.  **Run `project_1_ai_chatbot_without_memory/ui.py`:** Show the "Caramel AI" persona. Ask a complex AI question and watch it simplify it for a "10-year-old."
2.  **Run `project_7_ai_ragbot_with_vector_db/app.py`:** Ask about the Chief AI Scientist. Show how the bot retrieves specific facts that weren't in its training data.

---

## 📝 8. Assessment & Evaluation (IIT Context)
*   **The "Agent" Question:** "If we wanted this bot to not just *answer* but *execute* a Python script based on its findings, what tool-calling library would we integrate next?"
*   **The Ethics Question:** "How do we handle bias in local models when there are no corporate guardrails?"

---

## 📢 9. Closing Statement
> "Generative AI is the new electricity, but Local RAG is the power grid that ensures it reaches the right destination safely. At IIT, we don't just use AI; we architect its ethics and its execution."

---

### 📚 Recommended Reading
*   *LangChain: Decentralized Orchestration*
*   *Vaswani et al: Attention is All You Need (The Foundation)*
*   *Local AI Manifesto: Sovereignty in the Age of Intelligence*

---
**Organization:** HERE AND NOW AI
**Slogan:** "AI is Good"
**Project URL:** [github.com/hereandnowai/chatbot-rag-and-finetuning-updated-for-2026](https://github.com/hereandnowai/chatbot-rag-and-finetuning-updated-for-2026)
