# 🆚 Multi-LLM Comparison System

> *"Don't guess which AI is better — benchmark it."*

<a href="https://multi-llms-comparison-system-ehezxqgiznsvnbuvvycu8w.streamlit.app/" target="_blank">
  <img src="https://img.shields.io/badge/🚀 Live Demo-Click Here-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
</a>

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=16&pause=1000&color=00D4FF&width=600&lines=Gemini+2.5+Flash+vs+Llama+3.1+8B+vs+DeepSeek+V3;One+Prompt.+Three+Models.+Real+Metrics.;Built+for+Engineers+who+take+AI+seriously." />

---

## 💡 The Problem I Solved

Every developer using LLMs faces the same question:

**"Which model should I use for this?"**

Switching between ChatGPT, Gemini, and Groq tabs, copy-pasting the same prompt, manually comparing outputs — it's slow, inconsistent, and unscientific.

**This project fixes that.**

Type your prompt once. Get responses from **3 frontier LLMs simultaneously** with objective metrics to back your choice.

---

## ⚡ Under The Hood

```
Your Prompt
    │
    ├──▶  gemini_model.py   ──▶  Gemini 2.5 Flash    (Google AI)
    ├──▶  groq_model.py     ──▶  Llama 3.1 8B        (Groq)
    └──▶  openrouter.py     ──▶  DeepSeek V3          (OpenRouter)
                │
                ▼
          metrics.py
    ┌─────────────────────┐
    │  ⏱ Response Time    │
    │  📝 Word Count      │
    │  🏆 Best Model Pick │
    └─────────────────────┘
                │
                ▼
    Streamlit Dark Dashboard
```

---

## 🧰 Built With

```python
tech = {
    "language"  : "Python 3.10+",
    "ui"        : "Streamlit (Dark Theme)",
    "llm_1"     : "Gemini 2.5 Flash  →  Google AI API",
    "llm_2"     : "Llama 3.1 8B      →  Groq API",
    "llm_3"     : "DeepSeek V3       →  OpenRouter API",
    "metrics"   : "Custom evaluation engine (metrics.py)",
    "config"    : "python-dotenv  |  .env  |  zero hardcoding"
}
```

---

## 📂 File Structure

```
multi-llms-comparison-system/
│
├── app.py            ← Streamlit UI + orchestration logic
├── gemini_model.py   ← Google Gemini 2.5 Flash handler
├── groq_model.py     ← Llama 3.1 via Groq handler
├── openrouter.py     ← DeepSeek V3 via OpenRouter handler
├── metrics.py        ← Scoring: time · words · performance
├── .env.example      ← API key template (safe to share)
└── requirements.txt
```

---

## 🚀 Run It Yourself

**Step 1 — Clone**
```bash
git clone https://github.com/BhairavThakare08/multi-llms-comparison-system.git
cd multi-llms-comparison-system
```

**Step 2 — Install**
```bash
pip install -r requirements.txt
```

**Step 3 — Add API Keys**
```bash
# Create your .env file
GEMINI_API_KEY      = your_key_here
GROQ_API_KEY        = your_key_here
OPENROUTER_API_KEY  = your_key_here
```
> 🔐 Keys stay in `.env` — never committed, never exposed.

**Step 4 — Launch**
```bash
streamlit run app.py
```

---

## 📊 What Gets Measured

| Metric | What It Tells You |
|---|---|
| ⏱ Response Time | Which model is fastest for production use |
| 📝 Word Count | Which model gives most detailed answers |
| 🏆 Performance Score | Overall winner across both dimensions |

---

## 🔭 What's Coming Next

```
▢  Add Claude 3.5, GPT-4o, Mistral to the comparison
▢  Token count + estimated API cost per response
▢  Export full benchmark report as PDF
▢  Prompt templates library for common use cases
▢  Public leaderboard across model versions
```

---

## 🙋‍♂️ Made By

**Bhairav Thakare** — AI & Data Science Engineering Student

Passionate about LLMs, RAG pipelines, and building things that actually work.

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bhairav-thakare-528137325)
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/BhairavThakare08)
[![Gmail](https://img.shields.io/badge/-Gmail-D14836?style=flat&logo=gmail&logoColor=white)](mailto:bhairavthakare@gmail.com)

---

