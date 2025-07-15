# 🪨 RockyBot: News Research Tool 📈

RockyBot is a simple Streamlit application that lets you perform **question-answering over news articles** by leveraging **LangChain**, **OpenAI embeddings**, and **FAISS vector search**. Just input up to 3 news URLs, and RockyBot will retrieve relevant answers based on the content of those pages.

---

## 🚀 Features

* 📄 Load news articles from provided URLs
* 🔍 Split content into meaningful text chunks
* 🧠 Generate embeddings using OpenAI
* 📦 Store/retrieve embeddings using FAISS vector index
* ❓ Ask questions and get source-based answers using a RetrievalQA chain
* 🧾 Source tracking for transparent results

---

## 🛠️ Tech Stack

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [LangChain](https://www.langchain.com/)
* [OpenAI API](https://platform.openai.com/)
* [FAISS (Facebook AI Similarity Search)](https://github.com/facebookresearch/faiss)
* [Dotenv](https://pypi.org/project/python-dotenv/)

---

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/rockybot.git
cd rockybot
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up `.env` file**

Create a `.env` file in the root directory with your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 🧪 Usage

Run the app with:

```bash
streamlit run app.py
```

Then:

1. Input up to 3 news URLs in the sidebar.
2. Click `Process URLs` to fetch and vectorize the content.
3. Type your question in the input box.
4. RockyBot will answer your question with sources.

---

## 🧠 How It Works

1. **WebBaseLoader** scrapes the content from the URL.
2. **RecursiveCharacterTextSplitter** splits the content into chunks.
3. **OpenAIEmbeddings** generates vector representations of those chunks.
4. **FAISS** indexes the vectors for fast retrieval.
5. **RetrievalQAWithSourcesChain** uses a language model (via ChatOpenAI) to answer user queries with source tracking.

---

## 📁 File Structure

```
rockybot/
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── .env                  # Your OpenAI API Key (not included in repo)
├── faiss_store_openai.pkl # Saved FAISS index (generated after first run)
```

---

## ✅ Example Questions

* "What is the main topic of the article?"
* "Who is mentioned in the news?"
* "What are the key takeaways?"

---

## 📌 Notes

* Only the **first URL** is currently processed (URLs 2 and 3 are ignored).
* The FAISS index is saved locally as `faiss_store_openai.pkl`.
* You may need to delete or refresh the FAISS index if input URLs change.

