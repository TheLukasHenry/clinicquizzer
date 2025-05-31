# ClinicQuizzer Project Brief

## Project Overview

ClinicQuizzer is an AI-powered interview and assessment platform designed for healthcare education, specifically focused on clinical knowledge evaluation. The system uses large language models and retrieval-augmented generation to create adaptive, domain-specific interviews that test candidate knowledge while providing structured scoring.

## Key Objectives

- Develop a specialized clinical interview system using domain-specific knowledge
- Create adaptive questioning that responds to candidate answers
- Implement real-time competency scoring on a 0-10 scale
- Provide detailed, competency-based feedback to improve educational outcomes

## Current Project Status

- Tasks 1-3, 5 are completed (environment setup, ChromaDB integration, document processing, RAG implementation)
- Tasks 4, 6-10 are pending (competency framework, interview session, scoring, UI/visualization, admin features)

## Project Timeline

- MVP focused on core interview functionality and basic scoring
- Future enhancements planned for analytics, LMS integration, and customization

## Key Stakeholders

- Clinical Students/Residents: Medical, dental, nursing or other healthcare students
- Clinical Educators: Faculty configuring assessments and reviewing performance
- Program Administrators: Staff managing the platform and reporting

## Technical Foundation

- Frontend: Open WebUI chat interface
- Backend: Custom Pipe Function for interview logic
- Vector Database: ChromaDB with SQLite
- LLM: OpenBioLLM model via Ollama
- Embedding Model: sentence-transformers/all-MiniLM-L6-v2

## Success Metrics

- Interview Completion Rate: >95%
- Scoring Correlation: >85% agreement with expert evaluators
- User Satisfaction: >4/5 rating
- Knowledge Retrieval Relevance: >90% relevance
