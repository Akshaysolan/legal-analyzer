import streamlit as st
from rag_pipeline import process_document, create_qa_chain
from ml.risk_detector import detect_risk
import os

def show_analyzer():
    # Header with analyzer button
    st.markdown("""
    <div style="display:flex; justify-content:space-between; align-items:center;">
        <h1>AI Legal Document Analyzer</h1>
        <button style="padding:8px 16px; background-color:#4B0082; color:white; border:none; border-radius:5px;">
            Analyze Document
        </button>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar for API key
    api_key = st.sidebar.text_input("Groq API Key", type="password")
    if api_key:
        os.environ["GROQ_API_KEY"] = api_key

    # File uploader
    uploaded_file = st.file_uploader("Upload Legal PDF", type="pdf")

    if uploaded_file:
        with st.spinner("Processing document..."):
            vectorstore = process_document(uploaded_file)
            qa_chain = create_qa_chain(vectorstore)

        # Query input
        query = st.text_input("Ask question about document")
        if query:
            response = qa_chain.invoke({"query": query})

            st.subheader("Answer")
            st.write(response["result"])

            # Risk detection
            risk = detect_risk(response["result"])
            st.subheader("Risk Score")
            st.write(f"{risk}/5")

            # Show source chunks
            st.subheader("Source Chunks")
            for doc in response["source_documents"]:
                st.write(doc.page_content[:300])
                st.write("---")