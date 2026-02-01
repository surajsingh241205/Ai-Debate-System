# AI Debate System  
### Multi-Agent LLM Application

An intelligent multi-agent debate platform where AI agents analyze a topic from opposing perspectives and a neutral judge evaluates the arguments and assigns scores.

This project demonstrates structured reasoning, adversarial analysis, and AI-based decision evaluation using modern Large Language Model (LLM) orchestration.

---

## Features

- **Multi-Agent Reasoning**
  - Agent A supports the statement
  - Agent B opposes the statement
  - Judge evaluates both sides neutrally

- **AI Score Meter**
  - Each agent receives a score (0–100)
  - Winner is declared with justification

- **Judge-Based Evaluation**
  - Structured verdict with logical explanation

- **Clean SaaS-Style UI**
  - Card-based layout
  - Clear separation of arguments
  - Professional dashboard appearance

- **Fast LLM Inference**
  - Powered by Groq LLM API

---

## System Architecture
```
User Input (Topic)
↓
Agent A (Supports Statement)
Agent B (Opposes Statement)
↓
Judge Agent (Evaluation + Scoring)
↓
Score Meter + Final Verdict
```

Each agent operates independently with a dedicated role prompt, ensuring unbiased and structured reasoning.

---

## Tech Stack

- **Backend:** Python, Flask  
- **LLM Engine:** Groq (LLaMA family)  
- **Frontend:** HTML, CSS  
- **Architecture:** Multi-agent reasoning system  
- **Environment:** Python virtual environment  

---

## Project Structure

```
AI-Debate-System/
├── .env                  # Environment variables (sensitive data)
├── requirements.txt      # Project dependencies
├── README.md             # Project description and instructions (CRITICAL)
├── LICENSE               # License information (important for open source)
├── app.py                # Main application entry point
├── core/
│   ├── __init__.py       # Makes 'core' a Python module
│   └── llm_engine.py     # Handles LLM interactions
├── agents/
│   ├── __init__.py       # Makes 'agents' a Python module
│   ├── pro_agent.py      # Logic for the 'pro' debater
│   ├── con_agent.py      # Logic for the 'con' debater
│   └── judge_agent.py    # Logic for the judge
├── frontend/             # Dedicated directory for web interface assets
│   ├── templates/
│   │   └── index.html    # HTML templates
│   └── static/
│       └── css/
│           └── style.css # CSS files
└── tests/                # Directory for unit and integration tests (RECOMMENDED)
    ├── test_agents.py
    └── test_core.py
```

---

## Create virtual environment
``` python -m venv venv ```
``` venv\Scripts\activate ```

## Install dependencies
``` pip install -r requirements.txt ```

## Configure environment variables
- Create a .env file:

``` GROQ_API_KEY=your_api_key_here ```

## Run the application
``` python app.py ```

### Open in browser:
``` http://127.0.0.1:5000 ```

---

### Example Debate Topics
- AI will replace software engineers in the next 10 years
- College degrees are becoming less valuable in the age of AI
- Remote work reduces long-term productivity

--- 

### Why This Project?
This is not a simple chatbot.
#### It demonstrates:
- Role-based LLM orchestration
- Adversarial reasoning design
- AI evaluation systems
- Structured prompt engineering
- Product-oriented architecture
### This pattern is applicable to:
- Decision-support systems
- Interview practice tools
- AI debate simulators
- Evaluation frameworks

---
### Author
**Suraj Singh**
**AI • Data Science • Full-Stack Development**

***Built as a portfolio-grade project to demonstrate real-world AI system design using multi-agent reasoning.***