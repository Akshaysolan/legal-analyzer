import streamlit as st
from rag_pipeline import process_document, create_qa_chain
from ml.risk_detector import detect_risk
import os

def show_analyzer():

    st.title("AI Legal Document Analyzer")

    api_key = st.sidebar.text_input("Groq API Key",type="password")

    if api_key:
        os.environ["GROQ_API_KEY"] = api_key

    uploaded_file = st.file_uploader("Upload Legal PDF",type="pdf")

    if uploaded_file:

        with st.spinner("Processing document..."):

            vectorstore = process_document(uploaded_file)
            qa_chain = create_qa_chain(vectorstore)

        query = st.text_input("Ask question about document")

        if query:

            response = qa_chain.invoke({"query":query})

            st.subheader("Answer")
            st.write(response["result"])

            risk = detect_risk(response["result"])

            st.subheader("Risk Score")
            st.write(f"{risk}/5")

            st.subheader("Source Chunks")

            for doc in response["source_documents"]:
                st.write(doc.page_content[:300])
                st.write("---")