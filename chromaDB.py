import json
from pathlib import Path
from langchain_community.document_loaders import JSONLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document

# --- Configuration ---
PSYCHO_CONCEPTS_FILE = 'psycho_concepts.json'
MEDITATION_SCRIPTS_FILE = 'meditation_scripts.json'
CHROMA_DB_PATH = './chroma_db'
COLLECTION_NAME = 'well_being_collection'

# --- 1. Define Helper Functions ---
def load_and_transform_json(file_path: str):
    """
    Loads JSON data from a file and transforms it into a list of Document objects.
    This function handles both psycho-concepts and meditation scripts correctly.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    documents = []

    if "psycho_concepts" in file_path:
        for concept_data in data.get("concepts", []):
            # The core content for embedding is the 'explanation'
            content = concept_data.get("explanation", "")
            # The entire JSON object is stored as metadata
            metadata = concept_data
            documents.append(Document(page_content=content, metadata=metadata))
    
    elif "meditation_scripts" in file_path:
        # Assuming data is a dictionary with a key "meditation_scripts"
        # that holds the list of script objects.
        for script_data in data.get("meditation_scripts", []):
            # The 'script' field is a list of strings (bullet points)
            script_list = script_data.get("script", [])
            
            # Join the list of bullet points into a single string
            full_script_content = " ".join(script_list)
            
            # Use a copy of the original object as metadata
            metadata = script_data.copy()
            # Remove the 'script' list from metadata to avoid redundancy
            metadata.pop('script', None) 
            
            documents.append(Document(page_content=full_script_content, metadata=metadata))
    
    return documents

def create_and_populate_chromadb(documents, db_path, collection_name):
    """
    Initializes an embedding model and creates a persistent ChromaDB collection.
    """
    # Initialize the embedding model (same one used in the main application)
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")

    print(f"Creating or updating ChromaDB collection: '{collection_name}'...")
    print(f"Embedding and storing {len(documents)} documents...")
    
    # Use Chroma.from_documents to create the database from our loaded documents.
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=db_path,
        collection_name=collection_name
    )
    
    print("Database creation complete.")

# --- 2. Main Script Execution ---
if __name__ == "__main__":
    try:
        # Load and transform documents from both JSON files
        print(f"Loading documents from {PSYCHO_CONCEPTS_FILE}...")
        psycho_docs = load_and_transform_json(PSYCHO_CONCEPTS_FILE)
        print(f"Found {len(psycho_docs)} psychoeducational concepts.")
        
        print(f"Loading documents from {MEDITATION_SCRIPTS_FILE}...")
        meditation_docs = load_and_transform_json(MEDITATION_SCRIPTS_FILE)
        print(f"Found {len(meditation_docs)} meditation scripts.")
        
        # Combine all documents into a single list
        all_documents = psycho_docs + meditation_docs
        
        # Create the ChromaDB with the combined documents
        create_and_populate_chromadb(
            documents=all_documents,
            db_path=CHROMA_DB_PATH,
            collection_name=COLLECTION_NAME
        )
        
        print(f"Successfully created ChromaDB at '{CHROMA_DB_PATH}' with collection '{COLLECTION_NAME}'.")
        
    except FileNotFoundError as e:
        print(f"Error: A required JSON file was not found. Please ensure '{e.filename}' exists in the same directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")