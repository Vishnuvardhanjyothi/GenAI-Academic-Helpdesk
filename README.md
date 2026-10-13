# 🤖 GenAI Academic Helpdesk

## 📌 Project Overview

GenAI Academic Helpdesk is a web-based AI chatbot designed to help students find academic information from college PDF documents. It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information and generate answers to student questions.

## ✨ Features

- Answers student queries using college PDF documents.
- Retrieves relevant text using semantic search.
- Generates context-aware responses using a language model.
- Provides a simple web interface for interactive conversations.
- Supports academic topics such as library services, placements, hostel information, and examinations, depending on the uploaded documents.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **AI Framework:** LangChain
- **Language Model:** Hugging Face Transformers (FLAN-T5)
- **Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`)
- **Vector Database:** ChromaDB
- **Document Processing:** PyPDF

## ⚙️ How It Works

1. Loads academic information from PDF documents.
2. Splits the documents into smaller text chunks.
3. Converts the text chunks into embeddings.
4. Stores the embeddings in ChromaDB for similarity-based retrieval.
5. Retrieves relevant content when a student asks a question.
6. Uses the retrieved content to generate an answer.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Vishnuvardhanjyothi/GenAI-Academic-Helpdesk.git
cd GenAI-Academic-Helpdesk
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment on Windows

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add academic PDF documents

Place your permitted, non-confidential academic PDF documents in the `uploads` folder, following the folder structure expected by the application.

### 6. Run the application

```bash
python app.py
```

Open this address in your browser:

`http://127.0.0.1:5000/`

## 🎯 Project Objective

The objective of this project is to explore how Generative AI, document retrieval, and semantic search can be combined to make academic information easier for students to access.

## 🔮 Future Improvements

- Improve retrieval accuracy and answer relevance.
- Add source-document references to answers.
- Improve handling of questions that are not covered by the documents.
- Expand the academic knowledge base.
- Improve the user interface and error handling.

## 👨‍💻 Author

**Jothi Vishnuvardhan**

GitHub: [Vishnuvardhanjyothi](https://github.com/Vishnuvardhanjyothi)
