# Instructions.md

## Implementation Checklist

### Project Setup

- [x] **Step 1:** Fork and clone the [Open WebUI repository](https://github.com/open-webui/open-webui).
- [x] **Step 2:** Set up the local development environment (Docker recommended).
- [x] **Step 3:** Install and run Ollama locally with the openbiollm model.

### Domain Knowledge Integration (RAG)

- [ ] **Step 4:** Collect domain-specific documents (e.g., PDFs, textbooks) relevant to the target specialization.
- [ ] **Step 5:** Chunk the documents into manageable sections (200-500 tokens each) for efficient processing.
- [ ] **Step 6:** Set up an external vector database (e.g., ChromaDB or Qdrant) to store embeddings.
- [ ] **Step 7:** Use Open WebUI's built-in embedding support to embed the document chunks.
- [ ] **Step 8:** Populate the vector database with the embedded chunks.
- [ ] **Step 9:** Verify the embeddings and perform basic similarity searches to ensure accurate retrieval.

### Prompt Engineering & Interview Flow

- [ ] **Step 10:** Create initial interview system prompts tailored to the chosen domain.
- [ ] **Step 11:** Test simple chat interactions using the Open WebUI interface to ensure prompt effectiveness.
- [ ] **Step 12:** Design adaptive question prompts that instruct the LLM to ask follow-up questions based on the candidate's responses.
- [ ] **Step 13:** Implement prompt logic to retrieve domain-specific context from the vector database during interviews.
- [ ] **Step 14:** Validate the adaptive follow-up question generation using RAG context to ensure depth in candidate assessment.

### Interview Management

- [ ] **Step 15:** Store chat/interview history within Open WebUI for record-keeping and analysis.
- [ ] **Step 16:** Implement functionality to export interview transcripts for grading purposes.

### Scoring and Grading Implementation

- [ ] **Step 17:** Define a clear scoring rubric in a structured format (e.g., JSON) with categories and weightings.
- [ ] **Step 18:** Implement an API call or pipeline to invoke LLM-based scoring mechanisms.
- [ ] **Step 19:** Develop a grading prompt that clearly instructs the LLM to score each category and provide written feedback.
- [ ] **Step 20:** Test the initial scoring prompt manually to assess accuracy and consistency in evaluations.

### Integration of Scoring Module

- [ ] **Step 21:** Set up an endpoint or pipeline within Open WebUI to trigger scoring after interview completion.
- [ ] **Step 22:** Pass the interview transcript and scoring rubric as context to the LLM for evaluation.
- [ ] **Step 23:** Store the LLM-generated scoring results and written feedback securely.
- [ ] **Step 24:** Display the scoring results clearly within the Open WebUI interface for user review.

### Validation and Refinement

- [ ] **Step 25:** Conduct multiple test interviews to validate the system's functionality and effectiveness.
- [ ] **Step 26:** Analyze the LLM scoring results for consistency, clarity, and alignment with the defined rubric.
- [ ] **Step 27:** Refine prompts or RAG context retrieval methods based on feedback and observed performance.
- [ ] **Step 28:** Retest the system to ensure improvements in adaptive questioning and grading accuracy.
