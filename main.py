import streamlit as st
from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator

st.title("Atomic RAG Lab")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file and openai_api_key:
    loader = PyPDFLoader(uploaded_file)
    index = VectorstoreIndexCreator().from_loaders([loader])
    llm = OpenAI(openai_api_key=openai_api_key)
    query = st.text_input("Ask a question about the PDF")
    if query:
        response = index.query(query, llm=llm)
        st.write(response)
