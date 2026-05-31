# Chapter 2 - Development Environment

## Purpose of this Chapter

Set up the tools required for building LLM and AI Agent applications.

The objective is not to become an expert in Python, VS Code, Streamlit, or FastAPI.

The objective is to know enough to build Agentic AI applications.

---

## Python

Python is the primary programming language used throughout the book.

Important topics:

* Functions
* Classes
* Modules
* Packages
* Dictionaries
* Lists
* JSON Handling

Focus on writing practical code rather than learning every Python feature.

---

## VS Code

Primary development environment.

Useful features:

* File Explorer
* Integrated Terminal
* Git Integration
* Debugger
* Extensions

Recommended extensions:

* Python
* Pylance
* GitHub Copilot
* Jupyter

---

## Virtual Environments

Purpose:

Avoid package conflicts between projects.

Rule:

One project = One virtual environment

Example:

Building_LLM_Agent_Applications_ProcessIndustry
│
└── .venv

Common Commands:

Create:

uv venv

Activate (PowerShell):

.venv\Scripts\Activate.ps1

Install package:

uv pip install package_name

---

## NumPy

Purpose:

Efficient numerical calculations.

Typical usage:

* Arrays
* Matrix operations
* Mathematical computations

Often used underneath ML libraries.

---

## Pandas

Purpose:

Data manipulation and analysis.

Common operations:

* Read CSV
* Filter rows
* Aggregate data
* Clean data

Very important for industrial datasets.

---

## Streamlit

Purpose:

Convert Python scripts into web applications.

Mental Model:

Python Script
→
Web Application

Example Use Cases:

* Operator Dashboard
* Plant Assistant Interface
* Trend Analysis UI

---

## FastAPI

Purpose:

Expose Python functionality through APIs.

Mental Model:

Python Function
→
REST API

Example:

POST /ask

Used when integrating:

* Agents
* Databases
* Frontend Applications
* External Systems

---

## Typical Agent Architecture

User
↓
Streamlit UI
↓
FastAPI Backend
↓
Agent
↓
LLM
↓
Tools
↓
Database / RAG / APIs

This architecture will appear repeatedly in later chapters.

---

## Key Takeaways

1. Python is the implementation language.
2. VS Code is the development environment.
3. Use a virtual environment for every project.
4. Pandas handles industrial data.
5. Streamlit provides user interfaces.
6. FastAPI provides backend APIs.
7. Most AI applications use Streamlit + FastAPI + Agents.
