# ClinicQuizzer Active Context

## Current Development Focus

We are currently focusing on implementing the Competency Framework Model (Task 4), which is a prerequisite for the Interview Session Model and Flow (Task 6) and the Real-Time Competency Scoring (Task 7).

## Task 4: Create Competency Framework Model

- Status: Pending
- Priority: Medium
- Dependencies: Task 2 (ChromaDB Integration)

### Requirements

1. Define the schema for competency objects (id, name, description, weight)
2. Create the 10 clinical competencies based on standard medical education frameworks
3. Implement storage in the database
4. Create admin interface for viewing and potentially customizing competencies
5. Develop competency weighting system
6. Ensure competencies are accessible to the scoring system

### Test Strategy

Verify that all 10 competencies are correctly stored and can be retrieved. Test the weighting system to ensure it properly influences the scoring calculations.

## Next Steps in Development Sequence

1. Complete Competency Framework Model (Task 4)
2. Develop Interview Session Model and Flow (Task 6)
3. Implement Real-Time Competency Scoring (Task 7)
4. Create Custom Pipe Function for Open WebUI (Task 8)
5. Develop Scoring Reports and Visualization (Task 9)
6. Implement User Management and System Configuration (Task 10)

## Completed Tasks

- Task 1: Setup Open WebUI with Ollama and OpenBioLLM
- Task 2: Implement ChromaDB Vector Database Integration
- Task 3: Develop Document Processing Pipeline
- Task 5: Implement RAG for Domain Knowledge Retrieval

## Technical Considerations for Current Phase

- Need to design competencies that cover essential clinical knowledge areas
- Ensure competency schema is flexible enough for different clinical domains
- Consider how weights will be applied during the scoring process
- Integrate with existing ChromaDB implementation for storage
- Plan for future extensibility to customize competencies
