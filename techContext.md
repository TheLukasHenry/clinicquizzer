# ClinicQuizzer Technical Context

## System Architecture

### Components

- **Frontend**: Open WebUI chat interface for user interaction
- **Backend**: Custom Pipe Function for interview logic, integrated with Open WebUI
- **Vector Database**: ChromaDB for document storage and retrieval
- **LLM**: OpenBioLLM model via Ollama for question generation and scoring

### Data Models

- **Interview Session**: Tracks conversation state, questions asked, and scores
- **Knowledge Base**: Domain-specific documents with vector embeddings
- **Competency Framework**: Defined set of 10 clinical competencies with weights and descriptions
- **Scoring Report**: Structured assessment data showing performance by competency

### APIs and Integrations

- Integration with Ollama for local LLM inferencing
- ChromaDB integration for vector storage and retrieval
- Possible webhook integration for external reporting systems

## Infrastructure Requirements

- Local deployment with Docker support
- Moderate GPU requirements for running quantized OpenBioLLM model
- Storage capacity for document embeddings and interview transcripts

## Technical Specifications

- Vector Database: ChromaDB with SQLite backend
- Embedding Model: sentence-transformers/all-MiniLM-L6-v2
- LLM: OpenBioLLM (8B parameter model), quantized via Ollama
- Maximum Document Size: 20MB per file, 100MB total collection
- Interview Length: 5 questions per session, adaptive based on responses

## Development Stack

- Open WebUI (forked) for frontend and basic chat functionality
- Python for backend processing and LLM integration
- Docker for containerization and deployment
- ChromaDB for vector storage
- Ollama for LLM management

## Technical Challenges

- LLM context limitations may impact interview depth
  - Mitigation: Careful prompt engineering and document chunking strategies
- Scoring consistency across evaluations
  - Mitigation: Structured prompts and calibration with expert reviewers
- Optimizing RAG for clinical domain specificity
  - Mitigation: Domain-specific document preprocessing and chunking
