import streamlit as st
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain

def user_input(user_question):
    # Check if necessary session state variables are initialized
    if st.session_state.conversation is None:
        st.warning("Please process a PDF first.")
        return

    if st.session_state.vector_store is None:
        st.warning("Vector store is not initialized.")
        return

    try:
        # Prepare the input for the QA chain
        input_documents = st.session_state.vector_store.similarity_search(user_question)

        if not input_documents:
            st.warning("No relevant documents found.")
            return

        # Get response from the conversational chain
        response = st.session_state.conversation({
            "input_documents": input_documents,
            "question": user_question
        })
        
        # Extract the answer from the response
        answer = response.get('output_text', 'Answer not found.')
    except Exception as e:
        st.error(f"An error occurred while processing the question: {e}")
        return

    # Update conversation history and prepend new entry to conversation history
    st.session_state.chatHistory.insert(0, {"question": user_question, "answer": answer})

    # Display conversation history
    st.write("**Conversation History:**")
    for entry in st.session_state.chatHistory:
        st.write("**User Query:**", entry["question"])
        st.write("**App Response:**", entry["answer"])
        st.markdown("--------------------------------------------------")

def clear_vector_store():
    # Clear the vector store and reset session state variables
    st.session_state.vector_store = None
    st.session_state.conversation = None
    st.success("Vector store cleared and conversation chain reset.")

def clear_history():
    # Clear the conversation history
    st.session_state.chatHistory = []
    st.success("Conversation history cleared.")

def main():
    st.set_page_config(page_title="ETE Langchain PDF QA", page_icon=":book:")

    # Main header with color
    st.markdown("<h1 style='color: #ff6347; font-size: 38px;'>Smart, Fast, Accurate - PDF QA with Langchain 🦜️ & LLaMA-3.1 🦙</h1>", unsafe_allow_html=True)

    # Initialize session state variables if not already set
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = []
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = None

    # User question input
    user_question = st.text_input("Ask a question from the PDF files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        # Sidebar title with color
        st.markdown("<h2 style='color: #ff6347;'>App Menu</h2>", unsafe_allow_html=True)
        
        # Upload PDF files
        pdf_files = st.file_uploader("Upload your PDF files and click on the 'Submit & Process' button", type=["pdf"], accept_multiple_files=True)
        
        if st.button("Submit & Process"):
            if pdf_files:
                try:
                    with st.spinner("Processing..."):
                        # Extract text from PDFs
                        raw_text = get_pdf_text(pdf_files)
                        st.info("PDF Text Extracted.")
                        
                        # Chunk the text into smaller pieces
                        text_chunks = get_text_chunks(raw_text)
                        st.info("Text Chunking done.")
                        
                        # Create a vector store from the text chunks
                        vector_store = get_vector_store(text_chunks)
                        st.session_state.vector_store = vector_store
                        st.info("Vector DB created Successfully.")
                        
                        # Initialize the conversational chain
                        st.session_state.conversation = get_conversational_chain(vector_store)
                        st.success("Processing complete. FAISS Vector Store is ready. You can now start querying.")
                except Exception as e:
                    st.error(f"An error occurred during processing: {e}")
            else:
                st.warning("Please upload PDF files.")
        
        # Sidebar section for clearing vector store with colored header
        st.markdown("<h3 style='color:  #ff6347;'>Manage Vector Store</h3>", unsafe_allow_html=True)
        if st.button("Clear Vector Store"):
            clear_vector_store()

        # Sidebar section for clearing history with colored header
        st.markdown("<h3 style='color:  #ff6347;'>Manage History</h3>", unsafe_allow_html=True)
        if st.button("Clear History"):
            clear_history()
    
    # Add the credit section
    st.markdown("<hr>", unsafe_allow_html=True)  # Adds a horizontal line with HTML
    st.markdown("<h3 style='color: #2ca02c;font-size: 20px;'>App Created by: Parthebhan Pari</h3>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
