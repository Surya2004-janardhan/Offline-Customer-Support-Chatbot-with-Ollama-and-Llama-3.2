# Detailed Execution Plan

This document outlines the 7-phase detailed execution plan for building the Offline Customer Support Chatbot with Ollama and Llama 3.2.

## Phase 1: Environment Setup & Project Structure
**Objective:** Set up the required Python environment, external tools (Ollama), and the initial directory architecture necessary for the project.
* **Commit 1:** `chore: initialize project with empty prompts/ and eval/ directories`
* **Commit 2:** `docs: add initial README.md and placeholder setup.md files`
* **Commit 3:** `build: configure Python virtual environment and add requirements.txt`
* **Commit 4:** `chore: add .gitignore for venv, compiled code, and system artifacts`

## Phase 2: Data Preparation & Dataset Sourcing
**Objective:** Programmatically access the Ubuntu Dialogue Corpus, parse conversations, and adapt them into 20 reliable e-commerce queries.
* **Commit 1:** `feat(data): initialize script to fetch Ubuntu dialogue corpus`
* **Commit 2:** `data: draft first 10 adapted e-commerce customer queries`
* **Commit 3:** `data: draft remaining 10 adapted e-commerce customer queries`
* **Commit 4:** `feat(chatbot): integrate the 20 final adapted queries into chatbot.py`

## Phase 3: Prompt Engineering Templates
**Objective:** Define the system behavior and response formatting using generic (zero-shot) and targeted (one-shot) prompt templates.
* **Commit 1:** `feat(prompts): create zero_shot_template.txt with agent persona and instructions`
* **Commit 2:** `feat(prompts): create one_shot_template.txt with strict policy instructions`
* **Commit 3:** `feat(prompts): add a high-quality return policy example to one-shot template`
* **Commit 4:** `refactor(prompts): refine system prompts to minimize local model hallucinations`

## Phase 4: Core Chatbot API Integration
**Objective:** Implement the communication layer to successfully interface with the local Ollama LLM server.
* **Commit 1:** `feat(chatbot): scaffold chatbot.py with Ollama API constants and API logic`
* **Commit 2:** `feat(chatbot): implement query_ollama function for POST requests and JSON parsing`
* **Commit 3:** `fix(chatbot): add error handling for connection issues and malformed model responses`
* **Commit 4:** `refactor(chatbot): connect query list iteration to the Ollama API loop logic`

## Phase 5: Automated Evaluation Scripting
**Objective:** Automate the querying of 20 distinct scenarios through both templates and correctly logging the raw results.
* **Commit 1:** `feat(eval): implement robust file reading for prompt templates in chatbot.py`
* **Commit 2:** `feat(eval): construct main execution loop processing all 20 queries automatically`
* **Commit 3:** `feat(eval): integrate markdown table formatting capabilities for evaluation logging`
* **Commit 4:** `feat(eval): hook up raw output writing to eval/results.md file`

## Phase 6: Manual Scoring & Results Logging
**Objective:** Configure the results structure and populate manual scores measuring relevance, coherence, and helpfulness.
* **Commit 1:** `docs(eval): add grading rubric header and structural table into eval/results.md`
* **Commit 2:** `chore(eval): perform manual scoring on all zero-shot generated outputs`
* **Commit 3:** `chore(eval): perform manual scoring on all one-shot generated outputs`
* **Commit 4:** `chore(eval): review and finalize all manual scoring for quantitative consistency`

## Phase 7: Final Documentation & Reporting
**Objective:** Complete comprehensive analyses documenting findings between models and deliver final user-facing setups.
* **Commit 1:** `docs(report): draft introduction and detailed methodology sections in report.md`
* **Commit 2:** `docs(report): compile results analysis comparing zero-shot and one-shot performance`
* **Commit 3:** `docs(report): finalize conclusion and system limitations section within report.md`
* **Commit 4:** `docs: polish setup.md and README.md with comprehensive tool run instructions`
