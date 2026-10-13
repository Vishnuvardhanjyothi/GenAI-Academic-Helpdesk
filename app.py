from flask import Flask, request, jsonify, render_template
import os
import requests

print("🚀 Help desk...")


from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline

from transformers import pipeline

# 1. FLASK APP

app = Flask(__name__)



documents = []
pdf_folder = "uploads"
for file in os. listdir(pdf_folder):
    if file.endswith(".pdf"):
       pdf_path = os.path. join(pdf_folder, file)
       loader = PyPDFLoader(pdf_path)
       docs = loader. load()
       documents . extend(docs)

text_Splitter = RecursiveCharacterTextSplitter(
chunk_size=500,
chunk_overlap=100
)
docs = text_Splitter.split_documents(documents)

# # #

#embeddings
embedding = HuggingFaceEmbeddings(
   model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -
# Vector Database
vectorstore = Chroma. from_documents(
    docs,
    embedding
)

#
# Retriever

retriever = vectorstore. as_retriever(
    search_kwargs={"k": 4}

)

# Load LLM
generator = pipeline(
    "text2text-generation",

    model="google/flan-t5-base",

    max_length=150

)

llm = HuggingFacePipeline(
     pipeline=generator
)
# Create QA System

qa = RetrievalQA.from_chain_type(
llm=llm,
retriever=retriever,
chain_type="stuff",
return_source_documents=True
)

@app.route("/")
def home():

    return render_template("index.html")


# ----------------------------
# Ask Route
# ----------------------------

@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    if not data or "question" not in data:

        return jsonify({
            "answer": "Please send a question"
        }), 400

    question = data["question"].lower().strip()

    # Greetings

    if question in ["hai", "hello", "hey","hi"]:

        return jsonify({
            "answer": "Hello! 👋 Welcome to GenAI Academic Helpdesk."
        })

    # Thank You

    if "thank" in question:

        return jsonify({
            "answer": "You're welcome 😊"
        })

    # Bye

    if "bye" in question:

        return jsonify({
            "answer": "Goodbye 👋 Have a great day!"
        })

    # AI Query

    try:

        result = qa.invoke({
            "query": question
        })

        answer = result["result"]

        doc = result["source_documents"][0]

        source = os.path.basename(
            doc.metadata["source"]
        )

        page = doc.metadata.get("page", 0)

        return jsonify({

            "answer": answer,

            "source": source,

            "page": page
        })

    except Exception as e:
       print("ERROR:", e)

       return jsonify({
        "answer": "Sorry, something went wrong.",
        "error": str(e)
       }), 500


# ----------------------------
# Run Server
# ----------------------------

if __name__== "__main__":
    app.run(debug=True)