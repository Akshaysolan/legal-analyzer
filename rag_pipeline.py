from rag.loader import load_document
from rag.chunking import split_documents
from rag.embeddings import get_embeddings
from rag.vectorstore import create_vectorstore
from rag.retriever import get_retriever
from rag.llm import get_llm
from langchain.chains.retrieval_qa.base import RetrievalQA


def process_document(uploaded_file):

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    docs = load_document("temp.pdf")

    chunks = split_documents(docs)

    embeddings = get_embeddings()

    vectorstore = create_vectorstore(chunks, embeddings)

    return vectorstore


def create_qa_chain(vectorstore):

    retriever = get_retriever(vectorstore)

    llm = get_llm()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain