# AI Agent — Autonomous Software Builder

An **AI-powered multi-agent system** that can plan, architect, and code small software projects automatically.  
Powered by **GPT-3.5-Turbo** and inspired by **Lovable Clone**, this project demonstrates how AI agents can collaborate intelligently to turn natural language ideas into functional code.

---

## Overview

This project is built around a **3-part agent system**:

1. **Planner Agent** — Understands user intent, analyzes requirements, and generates a structured action plan.  
2. **Architect Agent** — Designs high-level architecture, data flow, and project structure based on the plan.  
3. **Coder Agent** — Implements the design by generating clean, executable code automatically.

All agents communicate seamlessly to create consistent and working outputs.

---

## Features

-  Multi-agent collaboration for software generation  
-  Converts natural-language prompts into runnable projects  
-  Auto-designs architecture and project structure  
-  Writes clean, modular Python or JavaScript code  
-  Iteratively refines results through feedback loops  

---

## Tech Stack

- **Model:** OpenAI GPT-4.1-Nano  
- **Language:** Python  
- **Tools:** Git, Virtualenv, VS Code  

---

## How to Use :
### Step 1 : Clone the repository
```bash
git clone https://github.com/Aditi-Verma-1709/AI-Agent.git
```
### Step 2 : Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
# or
venv\Scripts\activate        # Windows
```
### Step 3 : Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 4 : Add your Open AI Api Key
In .env file, add your Open AI API Key
```bash
OPENAI_API_KEY=your_api_key_here   
```
### Step 5 : Install Dependencies
Open graph.py and modify the user_prompt to describe the software you want the AI to build:
```bash
user_prompt = "Build a simple calculator."
```
### Step 6 : Install Dependencies
After editing your prompt, run the following in the terminal :
```bash
python graph.py
```
