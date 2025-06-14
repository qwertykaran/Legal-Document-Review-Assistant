from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings  # ✅ Changed
from dotenv import load_dotenv
import os
import utils as Utils

load_dotenv()

# ✅ Replaced OpenAIEmbeddings
embeddings = HuggingFaceEmbeddings()

# Load your document
loader = TextLoader("sample.txt")
documents = loader.load()

# Split into chunks
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(documents)

# Save to Chroma DB
Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=Utils.DB_FOLDER,
    collection_name="collection_1"
)

print("✅ Data added successfully!")
