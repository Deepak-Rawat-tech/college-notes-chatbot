import streamlit as st
from utils import get_answer

st.set_page_config(page_title="College Notes Chatbot", layout="wide")
st.title("📚 College Notes Chatbot")

st.markdown("Ask any question from your college notes 👇")

query = st.text_input("Enter your question")

if st.button("Ask"):
    if query:
        with st.spinner("Searching for answer..."):
            answer = get_answer(query)
            st.success(answer)
    else:
        st.warning("Please enter a question.")

