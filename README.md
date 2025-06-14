# Legal Document Review Assistant

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

An AI-powered tool that automates legal document review using LLMs and vector similarity search. It helps legal professionals quickly analyze documents by providing natural language answers based on document context.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Example Use Cases](#example-use-cases)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Features

### Core Capabilities
- **Document Processing**: Upload and parse legal documents (PDF, etc.)
- **Semantic Search**: Generate and store text embeddings for efficient retrieval
- **Context-Aware Answers**: Use Retrieval-Augmented Generation (RAG) to provide accurate responses
- **Multi-LLM Support**: Compatible with OpenAI, DeepSeek, and other LLM APIs
- **Modular Design**: Easy to extend with new document types or LLM providers

### Advanced Functionality
- FAISS-based vector similarity search
- Chunking and embedding optimization for legal texts
- Configurable similarity thresholds

## Tech Stack

- **Core Language**: Python 3.8+
- **Vector Search**: FAISS
- **LLM Integration**: OpenAI/DeepSeek APIs
- **Framework**: LangChain
- **Document Parsing**: PyPDF2, pdfminer
- **Environment Management**: pip/conda

## Installation

### Prerequisites
- Python 3.8 or later
- API key for your preferred LLM provider

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/legal-document-review-assistant.git
cd legal-document-review-assistant

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up your API key
echo "OPENAI_API_KEY=your_api_key_here" > .env
