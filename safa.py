import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from operator import itemgetter

# --- Global Setup and Constants ---
# Path to the ChromaDB directory
CHROMA_DB_PATH = "./chroma_db"

# --- 2. Helper Functions for LangChain Components ---
@st.cache_resource
def get_llm():
    """Load the local Ollama Llama 3 model for conversation."""
    return ChatOllama(model="safa")

@st.cache_resource
def get_retriever():
    """
    Set up the ChromaDB client and retriever.
    Assumes a pre-populated 'well_being_collection' exists.
    """
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    vector_store = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embeddings,
        collection_name="well_being_collection"
    )
    return vector_store.as_retriever()

# --- Main Streamlit Application Function ---
def main():
    """Main Streamlit application function."""
    
    st.set_page_config(page_title="Safa: Your Well-Being Assistant", page_icon="🧘‍♀️")
    st.title("Safa: Your Well-Being Assistant 🧘‍♀️")
    # st.write("Hello, I'm Safa. I'm here to listen and help you find clarity and inner peace. How are you feeling today?")

    # Initialize chat history in session state at the very beginning
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        # st.session_state.chat_history.append({"role": "assistant", "content": "Hello, I'm Safa. What's on your mind today?"})
        st.session_state.chat_history.append({"role": "assistant", "content": "Hello, I'm Safa. I'm here to listen and help you find clarity and inner peace. How are you feeling today?"})

    # 2. Display existing messages from chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # --- LangChain Runnable Definitions (can stay at the top level or inside main) ---
    # Prompt for the Conversational Core
    conversational_core_prompt = ChatPromptTemplate.from_template(
        """
        You are Safa, a compassionate and empathetic well-being assistant. Your name means "purity" or "serenity" in Arabic, reflecting your purpose to help users find inner peace.
        Your core role is to be a proactive listener. Do not simply respond; instead, actively encourage the user to explore their feelings by asking open-ended questions. Your responses should be thoughtful and non-judgmental.
        You can help the user by providing explanations of psychoeducational concepts and meditation exercises. You were created by Sherif Sakran, an MSc student at the University of Glasgow, who designed you to promote well-being through proactive engagement.

        Current conversation history:
        {chat_history}

        User: {user_message}
        Safa (emotion: calmness, intent: general_chat_intent):
        """
    )

    # The chain now accepts 'chat_history' as a direct input key.
    conversational_core_chain = (
        RunnablePassthrough.assign()
        | conversational_core_prompt
        | get_llm()
        | StrOutputParser()
    )

    # Prompt for the RAG System
    rag_prompt = ChatPromptTemplate.from_template(
        """
        You are Safa, a knowledgeable well-being assistant. You are an expert in psychoeducation and meditation.
        You will answer the user's question based ONLY on the provided context. If the context does not contain the answer, politely state that you cannot provide information on that topic.
        
        Context:
        {context}
        
        Question: {user_message}
        Safa:
        """
    )
    
    rag_chain = (
            RunnablePassthrough.assign(context=itemgetter("user_message") | get_retriever())
            | rag_prompt
            | get_llm()
            | StrOutputParser()
        )

    user_input = st.chat_input("Start a conversation...")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Classifying intent..."):
                llm = get_llm()
                intent_prompt = ChatPromptTemplate.from_template(
                    """
                    Analyze the user's message and classify their intent into one of the following categories:
                    - `venting_intent`: The user is expressing feelings or thoughts without seeking a direct solution.
                    - `continue_venting_intent`: The user is continuing a previous line of venting or expressing feelings.
                    - `seeking_answer_intent`: The user is clearly asking for advice, help, or a solution to their problem.
                    - `psychoeducational_knowledge_seeking_intent`: The user is asking for a specific psychoeducational concept.
                    - `meditation_request_intent`: The user is asking for a guided meditation or a meditation script.
                    - `greeting_intent`: The user is greeting or making small talk.
                    - `conversing_intent`: The user is making small talk.
                    - `asking_about_yourself_intent`: The user is asking about you, your capabilities, your purpose, and who created you.
                    - `other`: The intent does not fit any of the above.

                    User message: '{user_input}'
                    Classification from the above categories (as one word label):
                    """
                )
                intent_classifier_chain = intent_prompt | llm | StrOutputParser()
                intent = intent_classifier_chain.invoke({"user_input": user_input}).strip().lower().replace("`", "")
                print('Detected intent:', intent)
                
                placeholder = st.empty()
                placeholder.info("Classified intent: **" + intent + "**")
                # st.info(f"Detected Intent: **{intent}**")

            is_rag = False
            rag_placeholder = st.empty()
            if intent in ["psychoeducational_knowledge_seeking_intent", "meditation_request_intent"]:
                with st.spinner("Retrieving relevant information..."):
                    retriever = get_retriever()
                    retrieved_docs = retriever.get_relevant_documents(user_input)
                    placeholder.empty()
                    
                    # Display the full top document for debugging
                    if retrieved_docs:
                        rag_placeholder.success(f"Found {len(retrieved_docs)} relevant documents.")
                        # st.success(f"Found {len(retrieved_docs)} relevant documents.")
                        is_rag = True
                        top_doc = retrieved_docs[0]
                        with st.expander("Show Retrieved Document Details"):
                            st.subheader("Top Retrieved Document")
                            st.write("**Full Content:**")
                            st.code(top_doc.page_content)
                            st.write("**Full Metadata:**")
                            st.json(top_doc.metadata)
                    else:
                        rag_placeholder.warning("No relevant documents found. Proceeding with conversational core.")
                        # st.warning("No relevant documents found. Proceeding with conversational core.")
            if is_rag:
                with st.spinner("Generating response based on top match..."):
                    # Pass the retrieved documents as the 'context' to the RAG chain
                    response = rag_chain.invoke({
                        "user_message": user_input,
                        "context": retrieved_docs
                    })
            else:
                # spinner_text = "Safa is thinking..." if not 
                placeholder.empty()
                with st.spinner("Safa is thinking..."):
                    response = conversational_core_chain.invoke({
                        "user_message": user_input,
                        "chat_history": "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.chat_history])
                    })
            rag_placeholder.empty()
            st.write(response)
            
        st.session_state.chat_history.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()