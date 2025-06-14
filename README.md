# 🧑⚖️ Legal Document Review Assistant  
*AI-Powered Contract Analysis at Lightning Speed* ⚡  

[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT)  
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://www.python.org/)  
![RAG](https://img.shields.io/badge/Architecture-RAG-ff69b4?style=for-the-badge)  

```
+ Turns legal docs into searchable knowledge bases  
! Supports OpenAI, DeepSeek, and local LLMs  
- No more manual clause hunting!
```
# 🛠️ Tech Stack

### 🤖 AI/ML Core
| Component       | Technology                          |
|-----------------|-------------------------------------|
| LLM Framework   | LangChain • LlamaIndex              |
| Embeddings      | OpenAI/text-embedding-3-small       |
| Vector Store    | FAISS (local) • Pinecone (cloud)    |

### 📄 Document Processing
| Function        | Libraries                           |
|-----------------|-------------------------------------|
| PDF Parsing     | PyPDF2 • pdfminer.six              |
| Office Docs     | Unstructured.io • python-docx       |
| Text Cleaning   | BeautifulSoup • regex               |

### ⚙️ Infrastructure
| Layer           | Tools                               |
|-----------------|-------------------------------------|
| Environment     | Poetry • pip • virtualenv           |
| API             | FastAPI (future)                    |
| Deployment      | Docker (planned)                    |

### 🔍 Search & Retrieval
| Technology      | Use Case                            |
|-----------------|-------------------------------------|
| FAISS           | Local similarity search             |
| SentenceBERT    | Cross-encoder re-ranking            |
| BM25            | Sparse retrieval (future)           |

# 🌟 Features Preview
┌──────────────────────┬──────────────────────┬──────────────────────┐  
│   📄 Doc Processing  │   🔍 Semantic Search │   💬 Context-Aware   │  
│  (PDF, DOCX, etc.)   │  (FAISS/Pinecone)    │    Q&A (RAG)        │  
└──────────┬───────────┴──────────┬───────────┴──────────┬───────────┘  
           │                      │                      │  
           ▼                      ▼                      ▼  
┌──────────────────────┐┌──────────────────────┐┌──────────────────────┐  
│  Auto-chunking with  ││  Hybrid search with  ││  Multi-LLM Support   │  
│ legal-aware splitting││ metadata filtering   ││ (Switch models on fly)│  
└──────────────────────┘└──────────────────────┘└──────────────────────┘  
# 🛠️ Tech Stack Superpowers
Area	Tech
AI Core	LangChain • LlamaIndex
Search	FAISS • Sentence-Transformers
Parsing	PyPDF2 • pdfminer • Unstructured.io
UI	Streamlit (Coming Soon)
# 🚀 Quick Start
```
# 1. Clone with git  
git clone https://github.com/yourusername/legal-ai-assistant.git && cd legal-ai-assistant  

# 2. Setup environment (Poetry recommended!)  
poetry install  # or pip install -r requirements.txt  

# 3. Configure secrets  
echo "OPENAI_API_KEY=sk-your-key-here" > .env  
```
# 🎯 Use Case Examples
```
1. 🔍 *"Show all termination clauses in this contract"*  
2. 📑 *"Compare indemnification sections across these 5 agreements"*  
3. ⚖️ *"Explain this arbitration clause in plain English"*
```
# 📂 Project Anatomy
legal-ai-assistant/  
├── 📁 core/  
│   ├── agent.py       # AI reasoning engine  
│   └── retriever.py   # Hybrid search system  
├── 📁 web/            # Future Streamlit UI  
├── tests/             # pytest suite  
└── models/            # Custom fine-tuned models (optional)  
# :) What Makes Us Different?
! Legal-Specific Optimizations:  
+ Specialized text splitting for contracts (preserves clause boundaries)  
+ Pre-built prompt templates for common legal queries  
+ Redaction detection system (beta)
  
# 📜 License
MIT - But we'd love a shoutout if you use this in production! 🚀

# Made with ❤️ and Python
