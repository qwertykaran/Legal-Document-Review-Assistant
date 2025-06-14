from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os
import utils as Utils

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Load all legal docs from ./data
doc_paths = [f"data/{f}" for f in os.listdir("data") if f.endswith(".txt")]
all_docs = []
for path in doc_paths:
    loader = TextLoader(path)
    all_docs.extend(loader.load())

# Chunking
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(all_docs)

# Try to use OpenAIEmbeddings first, then fall back to HuggingFace
embeddings = None

try:
    from langchain_openai import OpenAIEmbeddings
    # Test quota by trying to embed a single dummy text
    test_embed = OpenAIEmbeddings(openai_api_key=api_key)
    test_embed.embed_documents(["This is a test."])  # check if quota exceeded
    embeddings = test_embed
    print("🔗 Using OpenAI embeddings.")
except Exception as e:
    print(f"⚠️ OpenAI Embeddings failed: {e}")
    print("➡️ Falling back to HuggingFace embeddings.")
    from langchain_community.embeddings import HuggingFaceEmbeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    print("🔗 Using HuggingFace embeddings (local).")

# Store in Chroma
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=Utils.DB_FOLDER,
    collection_name="collection_1"
)

vectorstore.persist()
print("✅ Legal documents ingested successfully.")
