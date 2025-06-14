from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import utils as Utils
import os

# Step 1: Load data
loader = TextLoader("sample.txt")  # Replace with actual file path
docs = loader.load()

# Step 2: Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
splits = text_splitter.split_documents(docs)

# Step 3: Create embeddings and save Chroma DB
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=embeddings,
    persist_directory=Utils.DB_FOLDER,
    collection_name="collection_1",
)

vectorstore.persist()
print("✅ Vector store rebuilt successfully!")
