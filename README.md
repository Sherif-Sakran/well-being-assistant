# Safa - The Well-Being-Assistant
## Tech
- Unsloth: to fast fine-tune the LLM
- Ollama: to run the LLM locally
- Langchain: to handle the conversation flow
- Streamlit: to develop the frontend
- ChromaDB: to vectorise the documents of the psychological concepts and meditation scripts to enable semantic search (i.e., RAG).

## LLMs
- Conversational: `unsloth/llama-3-8b-Instruct-bnb-4bit` was finetuned on both [well-being](full_dataset.json) and [personal info](personal_info_dataset.json) datasets.
- Embedding: `mxbai-embed-large`

## Dataset Prompts
All datasets were generated using Google Gemeni 2.5 Flash using the following prompts:
- [Well-Being](main_dataset_prompt.md)
- [Safa's Personal Info](personal_info_dataset_prompt.md)
- [Psychoeducational Concepts](psychoedu_concepts_dataset_prompt.md)
- [Meditation Scripts](meditation_dataset_prompt.md)

## Safa-Based Dialogue Sample
- [UofG Library ♥](<Safa_ Your Well-Being Assistant full dialogue.pdf>)