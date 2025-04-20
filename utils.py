import PyPDF2
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document

def load_pdf_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def get_qa_chain(text):
    chunks = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_text(text)
    docs = [Document(page_content=c) for c in chunks]
    chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")
    return lambda q: chain.run(input_documents=docs, question=q)
