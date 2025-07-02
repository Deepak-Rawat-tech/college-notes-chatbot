# 🤖 College Notes Chatbot

An AI-powered chatbot that converts academic PDF notes into structured question-answer (Q&A) format and intelligently answers student queries using Natural Language Processing (NLP).

---

## 📚 Overview

The chatbot extracts content from lecture notes in PDF format and generates a CSV file with questions and answers based on headings and key concepts. It then uses sentence embeddings and semantic similarity to respond to student queries with relevant answers — no manual tagging or training required!

---

## 🚀 Features

- 📄 Converts academic PDFs into a structured Q&A format
- 🧠 Uses NLP to match user questions with the most relevant answers
- 📥 Exports the output to a CSV file (`csv.csv`) for easy chatbot training
- 🔍 Intelligent query handling via semantic similarity and keyword extraction
- ⚡ Fully automated pipeline from PDF to chatbot-ready content

---

## 🛠️ Technologies Used

- **Python** – Backend and automation logic  
- **tabula-py** – Extracts tables and content from PDF files  
- **OpenAI API** – Generates human-like questions and answers from raw text  
- **Sentence Embeddings** – For matching questions semantically  
- **Pandas** – For CSV creation and data formatting  
- **Regex** – For text cleaning and heading detection

---

## 🧪 How It Works

1. **PDF Processing**:  
   `tabula-py` reads and extracts relevant content from the academic PDF.

2. **Chunking & Q&A Generation**:  
   The content is broken into logical sections (e.g., based on headings), and each chunk is turned into a question-answer pair using OpenAI.

3. **CSV Output**:  
   The Q&A pairs are stored in a CSV file named `csv.csv`.

4. **Query Matching**:  
   When a student asks a question, the chatbot uses sentence embeddings to find the most semantically similar question in the dataset and responds with the linked answer.

---

## 🖼️ Screenshot

![Image](https://github.com/user-attachments/assets/99f287d6-44f2-4e4d-8c83-e6ce634e1199)
![Image](https://github.com/user-attachments/assets/07f88610-0a69-481c-a326-ca26e1b91f7c)

---

## 📁 Folder Structure


