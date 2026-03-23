Generative AI Projects
A collection of Generative AI applications built from scratch while learning the Microsoft "Generative AI for Beginners" curriculum. Each project demonstrates different GenAI concepts and patterns.

Projects
1. Multi-Step Recipe Generator
Folder: text-generation-apps/app.py

A multi-step AI workflow that chains two LLM API calls — first generating a recipe from user input, then automatically extracting a shopping list from that recipe. Demonstrates token management, completion objects, and temperature tuning.

Key concepts: Multi-step LLM workflows, chained API calls, temperature control

2. AI Study Buddy
Folder: text-generation-apps/study_buddy.py

An interactive Python tutoring chatbot with full conversation history management. Includes UX best practices like loading indicators, input validation for cost optimization, error recovery with state management, and separated user-facing messages from developer logging.

Key concepts: Conversation memory, system message constraints, UX for AI apps, error recovery

3. Semantic Search Engine
Folder: search-apps/search_app.py

A semantic search system over 1,400+ YouTube video transcript chunks using text-embedding-3-small (1536-dimensional vectors). Implements cosine similarity scoring from scratch using NumPy for vector comparison and ranked retrieval.

Key concepts: Embeddings, cosine similarity, vector search, retrieval pipeline

4. AI Image Generator
Folder: image-generation-apps/

Image generation system using OpenAI's GPT Image API with metaprompt engineering for content safety. Includes disallow lists for child-safe content, base64 decoding pipeline, and modular architecture with separate generate and save functions.

Key concepts: Image generation API, metaprompts, content safety, defensive file management

5. AI Course Finder
Folder: function-calling/course_finder.py

An intelligent course recommendation system using OpenAI function calling. The LLM acts as a router — extracting structured arguments from natural language and triggering real API calls. Includes secure function dispatch and argument validation to prevent prompt injection.

Key concepts: Function calling, LLM as router, tool definitions, AI security, argument validation

Tech Stack
Python 3.14
OpenAI API (GPT-4o-mini for chat, text-embedding-3-small for embeddings)
NumPy for vector operations
Requests for external API calls
Setup
Clone this repo
Create a virtual environment: python -m venv .venv
Activate it: source .venv/bin/activate
Install dependencies: pip install -r requirements.txt
Copy .env.example to .env and add your API keys
Run any project: python text-generation-apps/app.py
Author
Tulasi Vishnu Vardhan Devineni

LinkedIn: https://www.linkedin.com/in/tulasi-devineni-813a101a2/
GitHub: https://github.com/Vishnu9704

