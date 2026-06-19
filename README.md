# 🦙 Multi-Agent Ollama Assistant

An AI-powered multi-agent system built using **Streamlit**, **Ollama**, **Llama 3**, and **MySQL**.

The application provides two intelligent agents:

- SQL Agent
- General Chat Agent

Users can ask questions in natural language, and the assistant either generates executable SQL queries or responds conversationally.


---

# 🚀 Features

### SQL Agent

✔ Converts Natural Language into SQL Queries

✔ Executes Generated Queries on MySQL Database

✔ Displays Results in Tabular Format

✔ Automatic Query Cleaning


---

### General Chat Agent

✔ Conversational AI Assistant

✔ Powered by Llama 3 through Ollama

✔ Answers General Knowledge Questions


---

# 🛠 Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python | Backend Logic |
| Streamlit | User Interface |
| Ollama | Local LLM Hosting |
| Llama 3 | Language Model |
| MySQL | Database |
| Pandas | Data Processing |
| Subprocess | Ollama Execution |


---

# 📂 Project Structure

```text

Multi-Agent-Ollama/

│── app.py

│── requirements.txt

│── README.md

│── schema.sql

```


---

# ⚙️ Working Architecture


User Input

↓

Agent Selection

↓

SQL Agent / Chat Agent

↓

Llama3 via Ollama

↓

Generated Response

↓

Display Output



---

# SQL Agent Workflow


User Question

↓

Schema Injection

↓

Prompt Engineering

↓

Llama3

↓

SQL Generation

↓

Query Cleaning

↓

MySQL Execution

↓

Result Display



---

# Chat Agent Workflow


User Question

↓

Prompt Construction

↓

Llama3

↓

Generated Response

↓

Display in Streamlit



---

# 🖥 Installation


### Clone Repository


```bash

git clone https://github.com/yourusername/Multi-Agent-Ollama.git

cd Multi-Agent-Ollama

```



### Install Dependencies


```bash

pip install -r requirements.txt

```


### Run Ollama


```bash

ollama run llama3

```


### Start Streamlit


```bash

streamlit run app.py

```



---

# Example Questions


### SQL Agent


Show all customers from USA


List top 10 products by price


Find total payments made in 2024



### Chat Agent


Explain Machine Learning


What is Deep Learning?


Tell me about Transformers



---

# Future Improvements


- Support multiple databases

- Add Memory Module

- RAG Integration

- PDF Question Answering

- OpenAI API Support

- Claude API Integration

- Gemini API Integration



---

# Author


Yogesh


Skills Demonstrated


✔ LLM Integration

✔ Prompt Engineering

✔ Multi-Agent Systems

✔ MySQL

✔ Streamlit

✔ Python

✔ Ollama

✔ Natural Language to SQL

✔ AI Application Development
