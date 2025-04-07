import os
import streamlit as st
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

def load_qchem_index(path: str = "quantum_chemistry_papers") -> GPTSimpleVectorIndex:
    """
    Build or load an index of quantum chemistry papers or resources.
    """
    index_file = "qchem_index.json"
    if os.path.exists(index_file):
        # Load existing index
        index = GPTSimpleVectorIndex.load_from_disk(index_file)
    else:
        # Otherwise, read docs from folder and build a new one
        docs = SimpleDirectoryReader(path).load_data()
        index = GPTSimpleVectorIndex.from_documents(docs)
        index.save_to_disk(index_file)
    return index

def main():
    st.title("Atomic RAG Lab")

    st.markdown("""
    **Welcome to the Atomic RAG Lab**  
    Ask about quantum chemistry topics: 
    electron density, UV-Vis transitions, molecular orbitals, etc.  
    This app uses a RAG approach to find relevant info from local papers.
    """)

    # Load or build index
    index = load_qchem_index("quantum_chemistry_papers")

    question = st.text_input("Your quantum chemistry question:")
    if st.button("Query"):
        if question.strip():
            response = index.query(question)
            st.write("**Answer:**")
            st.write(response)
        else:
            st.warning("Please enter a question.")

    st.markdown("---")
    st.info("**Note**: Make sure you have a 'quantum_chemistry_papers' folder with PDF/text docs if you want real data retrieval.")

if __name__ == "__main__":
    main()
