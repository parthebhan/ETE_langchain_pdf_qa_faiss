
# **Smart, Fast, Accurate - PDF QA with Langchain 🦜️ & LLaMA-3.1 🦙**

# **app.py**

### **Purpose**

This script provides a web interface using Streamlit to interact with a PDF Query System powered by Langchain and LLaMA-3.1. Users can upload PDF documents, query the content, and view responses. It integrates functionalities for processing PDFs, querying, and managing state within the Streamlit app.

### **Usage**

1. **Initialization**: The script initializes with a specific instruction.
2. **Processing**: Parses the PDF, converts content to markdown, and splits it into chunks.
3. **Vector Store**: Creates document embeddings and stores them in the Faiss vector database.
4. **QA System**: Sets up a QA system with ChatGroq to answer user queries based on the processed document.
5. **Querying**: Asks questions and displays response.

![Alt text](https://github.com/parthebhan/ETE_langchain_pdf_qa_faiss/blob/cc5f6f0fbd706d98b43d7dd9e14a38c6b037658c/App%20Preview.jpg)

### **Key Functions**

- **`user_input(user_question)`**
  - **Purpose**: Processes the user's question by querying the vector store and conversational chain.
  - **Workflow**: Checks if the PDF and vector store are initialized, performs a similarity search, retrieves and displays the answer, and updates the conversation history.

- **`clear_vector_store()`**
  - **Purpose**: Clears the vector store and resets the session state variables.
  - **Workflow**: Sets `st.session_state.vector_store` and `st.session_state.conversation` to `None`, and shows a success message.

- **`clear_history()`**
  - **Purpose**: Clears the conversation history.
  - **Workflow**: Sets `st.session_state.chatHistory` to an empty list and shows a success message.

- **`main()`**
  - **Purpose**: Orchestrates the app's workflow.
  - **Workflow**: Sets up Streamlit configuration, initializes session state variables, processes user inputs, handles PDF uploads, manages vector store and history, and displays app credits.

# **helper.py**

### **Purpose**

This module provides helper functions to extract text from PDFs, split text into chunks, create a FAISS vector store, and initialize a conversational chain using Langchain and ChatGroq. It integrates various AI models and utilities to support document-based question answering.

### **Key Functions**

- **`get_pdf_text(pdf_docs)`**
  - **Purpose**: Extracts text from a list of PDF files.
  - **Workflow**: Iterates through each PDF, extracts text from each page, and concatenates the results.

- **`get_text_chunks(text)`**
  - **Purpose**: Splits text into manageable chunks.
  - **Workflow**: Uses `RecursiveCharacterTextSplitter` to divide the text into chunks of 1000 characters with an overlap of 20 characters.

- **`get_vector_store(text_chunks)`**
  - **Purpose**: Creates a FAISS vector store from text chunks.
  - **Workflow**: Uses `GoogleGenerativeAIEmbeddings` to generate embeddings and stores them in a FAISS vector store.

- **`get_conversational_chain(vector_store)`**
  - **Purpose**: Creates a QA chain for question answering using the ChatGroq model.
  - **Workflow**: Defines a prompt template, initializes a `ChatGroq` model, and sets up a QA chain using `load_qa_chain` with the prompt template.


## **Summary**

This code integrates various AI and NLP tools to build a powerful system for interacting with PDF documents. It handles the entire pipeline, from parsing and storing document content to retrieving and answering user queries. The script is modular and extensible, offering a robust solution for document-based question-answering systems.

![Alt text](https://github.com/parthebhan/ETE_langchain_pdf_qa_faiss/blob/cc5f6f0fbd706d98b43d7dd9e14a38c6b037658c/conversational_retrieval_chain-5c7a96abe29e582bc575a0a0d63f86b0.png)

## **Process**

![Alt text](https://github.com/parthebhan/ETE_langchain_pdf_qa_faiss/blob/cc5f6f0fbd706d98b43d7dd9e14a38c6b037658c/process.png)

## **Author**

This script was created by Parthebhan Pari.

## **Notes**

- Ensure that the required API keys (Groq, LlamaParse, Google) are correctly configured in your environment variables.
- The script uses advanced AI models for parsing and answering questions, requiring a stable internet connection and sufficient computational resources.


### **🔗 Connect with Me**

Feel free to connect with me on :

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://parthebhan143.wixsite.com/datainsights)

[![LinkedIn Profile](https://img.shields.io/badge/LinkedIn_Profile-000?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/parthebhan)

[![Kaggle Profile](https://img.shields.io/badge/Kaggle_Profile-000?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/parthebhan)

[![Tableau Profile](https://img.shields.io/badge/Tableau_Profile-000?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/parthebhan.pari/vizzes)
