#import streamlit
import streamlit as st
import os
from dotenv import load_dotenv

# import pinecone
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

st.title("Chatbot")

# initialize pinecone database
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

# initialize pinecone database
index_name = os.environ.get("PINECONE_INDEX_NAME")  # change if desired
index = pc.Index(index_name)

# initialize embeddings model + vector store
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.environ.get("GOOGLE_API_KEY"),
    output_dimensionality=768
)
vector_store = PineconeVectorStore(index=index, embedding=embeddings)

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# display chat messages from history on app rerun
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# create the bar where we can type messages
prompt = st.chat_input("How are you?")

# did the user submit a prompt?
if prompt:

    # add the message from the user (prompt) to the screen with streamlit
    with st.chat_message("user"):
        st.markdown(prompt)

        st.session_state.messages.append(HumanMessage(prompt))

   # initialize the llm
    llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.environ.get("GROQ_API_KEY")
)

   # creating and invoking the retriever
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 8},
)

    docs = retriever.invoke(prompt)

    print("FOUND DOCS:", len(docs))

    for i, d in enumerate(docs):
        print(f"\n----- DOC {i+1} -----")
        print(d.page_content[:500])


    docs_text = "\n\n".join(d.page_content for d in docs)

    system_prompt = """
You are a GlobalFreight policy assistant.

Answer the user's question ONLY using the context below.

Rules:
- Never use outside knowledge.
- Never guess.
- Do not give general logistics explanations.
- Use exact values, categories, refunds, time limits, and escalation rules from the document.
- If the answer is missing, reply exactly:
"I do not know based on the provided documents."

Context:
{context}
"""

    # Populate the system prompt with the retrieved context
    system_prompt_fmt = system_prompt.format(context=docs_text)


    print("-- SYS PROMPT --")
    print(system_prompt_fmt)

    # adding the system prompt to the message history
    st.session_state.messages.append(SystemMessage(system_prompt_fmt))

    # invoking the llm
    # result = llm.invoke(st.session_state.messages).content
    messages = [
    SystemMessage(system_prompt_fmt),
    HumanMessage(prompt)
   ]

    response = llm.invoke(messages)

    result = response.content

    token_usage = response.response_metadata.get(
        "token_usage",
        {}
    )


    # adding the response from the llm to the screen (and chat)
    with st.chat_message("assistant"):
        st.markdown(result)

        st.session_state.messages.append(AIMessage(result))

        st.write("Token usage:")
        st.json(token_usage)
