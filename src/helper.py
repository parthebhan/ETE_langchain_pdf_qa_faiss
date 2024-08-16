import os
from PyPDF2 import PdfReader

from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores.faiss import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ['GROQ_API_KEY'] = GROQ_API_KEY

def get_pdf_text(pdf_docs):
    """
    Extracts text from a list of PDF files.
    """
    text = ""
    for pdf in pdf_docs:
        try:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text() or ""
        except Exception as e:
            print(f"Error reading {pdf}: {e}")
    return text

def get_text_chunks(text):
    """
    Splits text into chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    """
    Creates a FAISS vector store from text chunks using Google Palm embeddings.
    """
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store



def get_conversational_chain(vector_store):
    """
    Creates a QA chain for question answering using the ChatGroq model and FAISS vector store.
    """
    prompt_template = """
    Answer the question as detailed as possible from the provided context. Make sure to provide all the details. If the answer is not in
    the provided context, just say, "Answer is not available in the context." Do not provide a wrong answer.\n\n
    Context:\n {context}\n
    Question:\n {question}\n

    Answer:
    """

    llm = ChatGroq(model="llama-3.1-70b-versatile", temperature=0)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    
    # Ensure that `load_qa_chain` is compatible with the `ChatGroq` model
    chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)

   
    return chain