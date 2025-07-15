# Standard imports
import os
import time
import streamlit as st
from dotenv import load_dotenv
import pickle

from langchain_text_splitters import RecursiveCharacterTextSplitter     # Break text into manageable chunks
from langchain_openai import OpenAIEmbeddings, ChatOpenAI               # Embeddings and LLM via OpenAI

from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS

# Load environment variables (e.g., OPENAI_API_KEY)
load_dotenv()

st.title("RockyBot: News Research Tool 📈")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store_openai.pkl"

main_placeholder = st.empty()
llm = ChatOpenAI(temperature=0.8, max_tokens=500)

if process_url_clicked:
    # Load data from URLs
    print("..",urls)
    data =WebBaseLoader(urls[0]).load()
    # loaders = UnstructuredURLLoader(urls=list_urls)
    # loaders = [WebBaseLoader(url).load() for url in list_urls]

    # split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = text_splitter.split_documents(data)
    # create embeddings and save it to FAISS index
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)

    # Save the FAISS index to a pickle file
    # with open(file_path, "wb") as f:
    #     pickle.dump(vectorstore_openai, f)
    
    vectorstore_openai.save_local(file_path)
        # vectorstore = pickle.load(f)

query = main_placeholder.text_input("Question: ")
# query = main_placeholder.text_input("Question: ")

if query:
    if os.path.exists(file_path):
        # Recreate the embedding function used during saving
        embeddings = OpenAIEmbeddings()

        # Load the FAISS index from local folder
        vectorstore = FAISS.load_local(file_path, embeddings,allow_dangerous_deserialization=True)

        # Create retrieval QA chain
        chain = RetrievalQAWithSourcesChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever()
        )

        # Ask question and get result
        result = chain({"question": query}, return_only_outputs=True)

        # Display result
        st.header("Answer")
        st.write(result["answer"])

        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            sources_list = sources.split("\n")
            for source in sources_list:
                st.write(source)



