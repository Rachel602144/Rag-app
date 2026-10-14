# Freight Policy Assistant — RAG Chatbot

A Retrieval-Augmented Generation (RAG) application that answers freight and logistics policy questions using a collection of reference documents. Built with Python, LangChain, Pinecone, Google Gemini embeddings, Groq, and Streamlit.

## Overview

Finding specific information in logistics policies, service-level agreements, customs references, and shipment-delay guidelines can require manually searching through multiple documents.

This project uses Retrieval-Augmented Generation (RAG) to retrieve relevant document passages and provide context-grounded answers through a conversational interface.

Instead of relying solely on the language model's general knowledge, the application retrieves relevant text from a vector database and supplies it as context to the model. The chatbot is instructed to answer only from that context and to respond with a fixed message when the required information is missing.

## Features

- **Document Ingestion:** Load Markdown documents from a local directory.
- **Text Chunking:** Split documents into smaller, overlapping chunks for retrieval.
- **Text Embeddings:** Generate vector embeddings using Google's Gemini embedding model.
- **Vector Database:** Store and retrieve document embeddings using Pinecone.
- **Semantic Search:** Retrieve relevant document passages based on a user's question.
- **Context-Grounded Responses:** Supply retrieved passages to the language model as context.
- **Conversational Interface:** Ask questions through a Streamlit chat interface.
- **Chat History:** Maintain conversation messages during the Streamlit session.
- **Token Usage Display:** Display token-usage metadata returned by the language model provider.
- **Configurable Cloud Services:** Use environment variables to configure API credentials and the Pinecone index.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic and orchestration |
| Streamlit | Interactive chatbot interface |
| LangChain | Document processing, embeddings, retrieval, and model integration |
| Pinecone | Cloud-based vector storage and similarity search |
| Google Gemini Embeddings | Convert text and queries into vector representations |
| Groq | Host and invoke the language model |
| Llama 3.1 8B Instant | Generate responses from retrieved context |
| python-dotenv | Load configuration from environment variables |

## Architecture

The project follows a document-ingestion and question-answering workflow.

### 1. Document Ingestion

The `ingestion.py` script loads Markdown files from the `documents/` directory using LangChain's `DirectoryLoader` and `TextLoader`.

The documents are split into chunks with the following configuration:

- **Chunk size:** 800 characters
- **Chunk overlap:** 400 characters

The overlap preserves some surrounding context between consecutive chunks.

### 2. Embedding Generation

The ingestion pipeline uses Google's `models/gemini-embedding-001` embedding model to convert document chunks into vector representations.

The embeddings are configured with an output dimensionality of 768.

### 3. Vector Storage

The generated embeddings are stored in a Pinecone index. The ingestion script creates the index if it does not already exist, using cosine similarity and an AWS serverless configuration in the `us-east-1` region.

### 4. Semantic Retrieval

The `retrieval.py` script connects to the existing Pinecone index, embeds a query, and retrieves the five most relevant document chunks using similarity search.

This script demonstrates the retrieval stage independently of the chatbot interface.

### 5. Response Generation

When a user submits a question through the Streamlit interface:

1. The application receives the question.
2. The question is used to retrieve the eight most relevant document chunks.
3. The retrieved passages are combined into a context string.
4. The context and question are passed to Groq's Llama 3.1 8B Instant model.
5. The generated response is displayed in the chat interface.
6. Available token-usage metadata is displayed alongside the answer.

The system prompt instructs the model to use only the retrieved context and return the following response when the answer is unavailable:

`I do not know based on the provided documents.`

## Knowledge Base

The repository contains three Markdown reference documents:

| Document | Purpose |
|---|---|
| `DOC1_carrier_sla_agreement.md` | Carrier service-level agreement reference |
| `DOC2_customs_tariff_reference.md` | Customs and tariff reference |
| `DOC3_shipment_delay_policy.md` | Shipment-delay policy reference |

These documents provide the knowledge base used by the ingestion pipeline.

## Project Structure

```text
Rag-app/
├── documents/
│   ├── DOC1_carrier_sla_agreement.md
│   ├── DOC2_customs_tariff_reference.md
│   └── DOC3_shipment_delay_policy.md
├── chatbot_rag.py
├── ingestion.py
├── retrieval.py
├── requirements.txt
├── README.md
└── .gitignore
```

- `ingestion.py` — Loads, chunks, embeds, and stores documents in Pinecone.
- `retrieval.py` — Tests semantic retrieval against the vector database.
- `chatbot_rag.py` — Implements the Streamlit chatbot and response-generation workflow.
- `documents/` — Contains the Markdown knowledge base.
- `requirements.txt` — Lists Python package dependencies.
- `.gitignore` — Defines files Git should exclude.

## Getting Started

### Prerequisites

- Python 3.11 or a compatible Python version
- A Pinecone account and API key
- A Google AI API key for Gemini embeddings
- A Groq API key for language-model inference

### 1. Clone the Repository

```bash
git clone https://github.com/Rachel602144/Rag-app.git
cd Rag-app
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_pinecone_index_name
GOOGLE_API_KEY=your_google_ai_api_key
GROQ_API_KEY=your_groq_api_key
```

Replace the example values with your own credentials.

**Security:** Do not commit `.env` or real API keys to GitHub. Keep credentials private and rotate any keys that have been exposed.

### 5. Ingest the Documents

From the project root, run:

```bash
python ingestion.py
```

This loads the Markdown documents, splits them into chunks, generates embeddings, and stores them in Pinecone.

Run ingestion before querying the chatbot so the vector database contains the reference documents.

### 6. Test Retrieval

Run:

```bash
python retrieval.py
```

The script executes a sample query and prints the retrieved document passages and metadata.

### 7. Launch the Chatbot

Run:

```bash
streamlit run chatbot_rag.py
```

Open the local URL provided by Streamlit in your browser and ask questions about the documents in the knowledge base.

## Example Questions

You can ask questions related to the information contained in the reference documents, such as:

- What service-level commitments are specified in the carrier agreement?
- What does the customs tariff reference say about a particular category?
- What procedures apply under the shipment-delay policy?
- What refund conditions or escalation rules are stated in the available documents?

The answers depend on the contents of the retrieved passages. If the required information is not present in the supplied context, the chatbot is instructed to say that it does not know based on the provided documents.

These are example questions, not verified answers from the knowledge base.

## Limitations

- The chatbot's answer quality depends on the completeness of the knowledge base and the relevance of retrieved chunks.
- The system does not currently display source citations or document references alongside answers.
- The current conversation history is maintained in Streamlit session state and is not persistent across independent sessions.
- The retrieval pipeline uses fixed values for the number of retrieved chunks and text chunking configuration.
- The application depends on external embedding, vector database, and language-model services.
- The current scripts do not include an automated evaluation suite for retrieval relevance or answer correctness.
- The current system prompt provides instructions against unsupported answers, but it does not guarantee that every generated response is factually correct.

## Future Improvements

- Display the source document and relevant passage for each answer.
- Add an evaluation dataset to measure retrieval quality and answer correctness.
- Experiment with chunk sizes, overlap, and retrieval parameters.
- Add reranking to improve the relevance of retrieved passages.
- Implement persistent conversation history when needed.
- Add error handling for API failures, missing credentials, and empty retrieval results.
- Add automated tests for ingestion, retrieval, and response generation.
- Provide a document-upload interface for updating the knowledge base.
- Deploy the application with secure credential management and appropriate access controls.

## Author

**Rachel Patni**

- [GitHub Profile](https://github.com/Rachel602144)
- [Project Repository](https://github.com/Rachel602144/Rag-app)

---

*This project demonstrates Retrieval-Augmented Generation, semantic search, vector databases, embedding models, prompt-based grounding, and LLM application development using Python.*
