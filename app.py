import streamlit as st
import os
from rag_pipeline import process_document, create_qa_chain
from ml.risk_detector import detect_risk

st.set_page_config(page_title="AI Legal Analyzer")
st.title("⚖️ AI Legal / Policy Document Analyzer")

api_key = st.text_input("Enter OpenAI API Key", type="password")

if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

uploaded_file = st.file_uploader("Upload Legal PDF", type="pdf")

if uploaded_file:

    st.success("Document Uploaded")

    with st.spinner("Processing document..."):
        vectorstore = process_document(uploaded_file)
        qa_chain = create_qa_chain(vectorstore)

    query = st.text_input("Ask a question about the document")

    if query:

        response = qa_chain.invoke({"query": query})

        st.subheader("Answer:")
        st.write(response["result"])

        risk_score = detect_risk(response["result"])

        st.subheader("Risk Score:")
        st.write(f"{risk_score} / 5")

        st.subheader("Source Chunks:")

        for doc in response["source_documents"]:
            st.write(doc.page_content[:300])
            st.write("---")