import os
from dotenv import load_dotenv

from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

load_dotenv()
#connect python code with pinecone vector database
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))


index_name = os.environ.get("PINECONE_INDEX_NAME") 

 #connect to existing Pinecone index containing embeddings
index = pc.Index(index_name)


embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.environ.get("GOOGLE_API_KEY"),
    output_dimensionality=768
)

#connect Pinecone storage with embedding model through LangChain
vector_store = PineconeVectorStore(index=index, embedding=embeddings)


retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 5
    }
)

#convert query to vector and search similar document chunks
results = retriever.invoke("what is retrieval augmented generation?")


print("RESULTS:")

for res in results:
    print(f"* {res.page_content} [{res.metadata}]")