import os 
import time  

from dotenv import load_dotenv 

from pinecone import Pinecone, ServerlessSpec  
from langchain_pinecone import PineconeVectorStore 
from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from langchain_core.documents import Document 
from langchain_community.document_loaders import DirectoryLoader,TextLoader  
from langchain_text_splitters import RecursiveCharacterTextSplitter 


load_dotenv()


pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))  # Connect application to Pinecone
index_name = os.environ.get("PINECONE_INDEX_NAME")  # Get Pinecone index name


existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]  
# Get list of already created Pinecone indexes


if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,   
        dimension=768,     
        metric="cosine",  
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ),                
    )

    while not pc.describe_index(index_name).status["ready"]:
        time.sleep(1)     


index = pc.Index(index_name)  # Connect to the created Pinecone index


embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001", 
    google_api_key=os.environ.get("GOOGLE_API_KEY"),
    output_dimensionality=768 
)


vector_store = PineconeVectorStore(
    index=index,
    embedding=embeddings
) # Connect Pinecone storage with embedding model through LangChain

loader = DirectoryLoader(
    "documents",        
    glob="*.md",       
    loader_cls=TextLoader
)


raw_documents = loader.load()  # Load documents into LangChain document format



text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,       
    chunk_overlap=400,    
    length_function=len, 
    is_separator_regex=False
)
documents = text_splitter.split_documents(raw_documents)  




i = 0
uuids = [] 
while i < len(documents):
    i += 1
    uuids.append(f"id{i}") 



vector_store.add_documents(
    documents=documents,
    ids=uuids
) 