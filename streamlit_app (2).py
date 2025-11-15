import streamlit as st
from transformers import pipeline

st.title("Free Text Summarizer (No API Key Needed)")

# Load summarizer model once
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

# Input text
source_text = st.text_area("Enter your text here", height=250)

if st.button("Summarize"):
    if not source_text.strip():
        st.error("Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarizer(source_text, max_length=150, min_length=40, do_sample=False)
            st.success(summary[0]['summary_text'])
