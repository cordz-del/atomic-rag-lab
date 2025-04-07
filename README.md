# atomic-rag-lab
Atomic RAG Lab - LLM that explains quantum chemistry

## Project Purpose

The Atomic RAG Lab is a Language Model (LLM) that explains quantum chemistry concepts. It allows users to upload PDFs related to quantum chemistry and ask questions about the content. The LLM leverages OpenAI's GPT-4 model to provide detailed explanations.

## Tech Stack

- LangChain
- OpenAI
- Streamlit
- LlamaIndex

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/cordz-del/atomic-rag-lab.git
   cd atomic-rag-lab
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

2. Open the app in your browser and upload a PDF related to quantum chemistry.

3. Ask questions about the content of the PDF and receive detailed explanations.

## Special Notes

- Ensure you have an OpenAI API key to use the GPT-4 model.
- The app may take a few moments to process large PDFs and generate responses.


## Live Demo

Check out the running app on [Hugging Face Spaces](https://huggingface.co/spaces/cordz-del/atomic-rag-lab).
