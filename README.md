# AI Repository-Aware Code Reviewer

An AI-powered repository-aware coding assistant built using Streamlit, ChromaDB, Sentence Transformers, AST parsing, and Google Gemini AI.

Upload Python files or complete repository ZIPs to perform AI-powered code reviews with semantic retrieval, repository-aware reasoning, static analysis, embeddings, and Retrieval-Augmented Generation (RAG).

The system intelligently analyzes code structure, indexes repositories into vector memory, retrieves semantically related functions across files, and generates contextual AI reviews.

---

# Features

* AI-Powered Code Reviews
* Multi-File Code Understanding
* Repository ZIP Ingestion
* Recursive Repository Traversal
* AST-Based Code Parsing
* Static Code Analysis
* Semantic Code Chunking
* ChromaDB Vector Memory
* Code Embedding Generation
* Repository-Aware Retrieval
* Cross-File Semantic Reasoning
* Streaming AI Responses
* Real-Time Repository Indexing
* Semantic Similarity Search
* Metadata-Enriched Retrieval
* Local Embedding Inference
* Modular AI Pipeline Architecture

---

# Tech Stack

## Frontend

* Streamlit

## AI / Retrieval Components

* Google Gemini API
* Sentence Transformers
* ChromaDB
* Transformers
* ONNX Runtime

## Code Intelligence

* Python AST
* Static Analysis
* Semantic Chunking

## Backend / Infrastructure

* Python
* Recursive File Traversal
* ZIP Repository Extraction
* Temporary Workspace Handling

---

# Project Architecture

```text
Repository ZIP Upload
        ↓
Repository Extraction
        ↓
Recursive File Traversal
        ↓
Python File Discovery
        ↓
AST Parsing
        ↓
Semantic Chunking
        ↓
Embedding Generation
        ↓
ChromaDB Vector Storage
        ↓
User Review Request
        ↓
Semantic Repository Retrieval
        ↓
Context Injection
        ↓
Gemini AI Review Generation
```

---

# Repository-Aware RAG Workflow

```text
Repository Upload
        ↓
Code Parsing
        ↓
Function Extraction
        ↓
Semantic Embeddings
        ↓
Repository Vector Memory
        ↓
User Code Review Query
        ↓
Cross-File Retrieval
        ↓
Repository Context Injection
        ↓
AI-Powered Review
```

---

# Folder Structure

```text
CODE-REVIEWER
│
├── embeddings
│   └── chroma_manager.py
│
├── prompts
│   └── review_prompt.txt
│
├── retrieval
│   └── retriever.py
│
├── services
│   └── llm_service.py
│
├── utils
│   ├── ast_analyzer.py
│   ├── code_chunker.py
│   ├── file_handler.py
│   ├── language_detector.py
│   ├── prompt_builder.py
│   ├── repo_ingestor.py
│   └── repo_zip_handler.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/decoded15/code-reviewer.git

cd code-reviewer
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Add Gemini API Key

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

# Running The Project

Start the Streamlit app:

```bash
streamlit run app.py
```

Application runs on:

```text
http://localhost:8501
```

---

# Static Analysis Features

The system performs AST-powered static analysis for:

* Syntax Validation
* Function Extraction
* Import Extraction
* Long Function Detection
* Deep Nesting Detection
* Import Complexity Analysis

---

# Semantic Retrieval System

The application builds repository-aware semantic memory using embeddings and ChromaDB.

Capabilities include:

* Cross-File Retrieval
* Semantic Function Matching
* Repository Context Injection
* Metadata-Aware Retrieval
* Similarity-Based Code Understanding

---

# Example Retrieval Flow

```text
auth.py
    ↓
validate_token()

login.py
    ↓
login()

        ↓

Semantic Retrieval

        ↓

AI understands authentication flow
across multiple files
```

---

# AI Engineering Concepts Learned

* Repository-Aware RAG
* Semantic Code Search
* Vector Databases
* Embeddings for Source Code
* AST Parsing
* Static Analysis
* Semantic Chunking
* Cross-File Retrieval
* Context Injection
* Retrieval-Oriented AI Systems
* Repository Indexing Pipelines
* Streaming AI Responses
* Local Embedding Inference
* ONNX Runtime
* Repository Traversal
* Metadata-Enriched Retrieval
* AI Orchestration Pipelines
* Retrieval-Centric AI Architecture
* Local AI Infrastructure

---

# Future Improvements

* GitHub Repository Cloning
* Multi-Language Support
* Symbol-Aware Retrieval
* Dependency Graph Analysis
* Repo Maps
* Agentic Debugging
* Local Code LLM Integration
* Ollama Integration
* Autonomous Code Editing
* Tool-Calling Agents
* Terminal Execution Sandboxing
* Memory Systems
* Multi-Agent Coding Workflows
* Docker Deployment

---

# Author

Built by Dibyansh (decoded15)
