import streamlit as st
from utils import load_code_files, chunk_text
from embed import create_embeddings
from endee_db import EndeeDB

st.title("💻 AI Codebase Assistant")

db = EndeeDB()

if st.button("Process Codebase"):
    data = load_code_files("codebase")

    if len(data) == 0:
        st.error("❌ No files found in codebase folder!")
    else:
        st.write("Files Loaded:", data)

        all_chunks = []
        paths = []

        for path, content in data:
            chunks = chunk_text(content)
            all_chunks.extend(chunks)
            paths.extend([path] * len(chunks))

        embeddings = create_embeddings(all_chunks)

        for emb, chunk, path in zip(embeddings, all_chunks, paths):
            db.insert(
                vector=emb,
                metadata={
                    "text": chunk,
                    "file": path
                }
            )

        st.session_state["db"] = db
        st.success("✅ Codebase processed!")

query = st.text_input("Ask about the code:")

if query and "db" in st.session_state:
    query_emb = create_embeddings([query])[0]
    results = st.session_state["db"].search(query_emb)

    for score, res in results:
        st.write(f"📄 File: {res['metadata']['file']}")
        st.code(res['metadata']['text'])
        st.write(f"Similarity: {score:.4f}")