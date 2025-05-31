# ClinicQuizzer System Patterns

## Core Architectural Patterns

### RAG (Retrieval-Augmented Generation)

- Vector embeddings of clinical documents stored in ChromaDB
- Similarity search to retrieve relevant context for question generation
- Context augmentation of prompts to ground LLM responses in factual information
- Implementation leverages sentence-transformers/all-MiniLM-L6-v2 for embeddings

### Adaptive Questioning Flow

- State tracking of conversation through interview sessions
- Analysis of previous responses to determine follow-up questions
- Dynamic adjustment of difficulty based on performance
- Limited to 5 questions per session for focused assessment

### Competency-Based Scoring

- Predefined framework of 10 clinical competencies
- Weighted evaluation of responses across multiple dimensions
- Consistent scoring methodology using structured LLM prompts
- Real-time calculation and aggregation of competency scores

## Design Principles

### Modularity

- Separation of document processing from interview logic
- Isolation of scoring mechanism from question generation
- Clear interfaces between components for maintainability

### Extensibility

- Support for multiple clinical domains and specialties
- Customizable competency frameworks
- Pluggable LLM backends for future model improvements

### User-Centered Design

- Simple, distraction-free assessment interface
- Clear visualization of performance metrics
- Intuitive document management for educators

## Data Flow Patterns

### Document Processing Pipeline

1. Document upload → Chunking → Embedding → Storage in ChromaDB
2. Maximum size limits: 20MB per file, 100MB total collection

### Interview Flow

1. Session initialization → Initial question → Student response →
2. Context retrieval → Response evaluation → Competency scoring →
3. Follow-up question generation → Repeat 5 times → Session summary

### Scoring Methodology

1. Response analysis → Evidence identification →
2. Individual competency scoring → Weighted aggregation →
3. Final competency profile generation
