from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import utils as Utils
import os

# Load environment variables
load_dotenv()

# Step 1: Load embeddings (HuggingFace - local and free)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Step 2: Load local LLM via Ollama
llm = OllamaLLM(model="llama3")

# Step 3: Load Chroma vectorstore
vectorstore = Chroma(
    persist_directory=Utils.DB_FOLDER,
    collection_name="collection_1",
    embedding_function=embeddings,
)

# Step 4: Create RetrievalQA chain with source return
retriever = vectorstore.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True  # ✅ Needed to get source filenames
)

# Step 5: Ask a question
while True:
    query = input("\nAsk a legal question (or type 'exit' to quit): ")
    if query.lower() in ("exit", "quit"):
        break

    response = qa_chain.invoke({"query": query})
    
    print("\n📌 Answer:\n", response['result'])
    print("\n📁 Sources:")
    for doc in response['source_documents']:
        print("-", os.path.basename(doc.metadata['source']))


