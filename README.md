# 🤖 AI Automation Agent

An AI Automation Agent built with **Google ADK** and **Gemini 2.5 Flash**. This project serves as the foundation for an intelligent automation assistant capable of performing real-world tasks using AI and Python.

## ✨ Features

- 💬 AI chat powered by Gemini 2.5 Flash
- 🧠 Built using Google ADK
- 🐍 Python 3.12
- 🔧 Easy to extend with custom tools

## 🛠️ Tech Stack

- Python 3.12
- Google ADK
- Gemini 2.5 Flash
- uv

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/fmaleeha/ai-automation-agent.git
cd ai-automation-agent
```

### Install dependencies

```bash
uv sync
```

### Configure your API key

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
```

You can obtain an API key from **Google AI Studio**.

### Run the project

```bash
uv run adk web my_agent
```

## 📁 Project Structure

```
my-ai-agent/
│── my_agent/
│   ├── __init__.py
│   └── agent.py
│── .gitignore
│── pyproject.toml
│── README.md
│── uv.lock
```

## 🎯 Roadmap

- [x] Basic AI Chat Agent
- [ ] Calculator Tool
- [ ] File Automation
- [ ] Weather Tool
- [ ] Gmail Integration
- [ ] Google Calendar
- [ ] PDF Chat
- [ ] SQLite Memory
- [ ] Multi-Agent System
- [ ] Cloud Deployment

## 📜 License

MIT License
