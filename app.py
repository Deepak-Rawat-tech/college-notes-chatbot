import streamlit as st
from utils import load_pdf_text, get_qa_chain
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="College Notes Chatbot")
st.title("📘 College Notes AI Chatbot")
st.write("Ask anything from your uploaded college notes!")

pdf_file = st.file_uploader("Upload PDF Notes", type="pdf")

if pdf_file:
    with st.spinner("Reading PDF..."):
        raw_text = load_pdf_text(pdf_file)
        chain = get_qa_chain(raw_text)
    
    query = st.text_input("Ask a question based on your notes:")
    
    if query:
        with st.spinner("Thinking..."):
            result = chain.run(query)
            st.success(result)
