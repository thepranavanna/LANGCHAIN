import streamlit as st
from sumy.parsers.plaintext import PlainTextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

st.title("Free Text Summarizer (No API Key, Streamlit Compatible)")

text = st.text_area("Enter text to summarize:", height=300)

if st.button("Summarize"):
    if not text.strip():
        st.error("Please enter some text.")
    else:
        parser = PlainTextParser.from_string(text, Tokenizer("english"))
        summarizer = LexRankSummarizer()

        summary_sentences = summarizer(parser.document, 5)   # 5 sentences summary

        summary = " ".join([str(sentence) for sentence in summary_sentences])

        st.subheader("Summary:")
        st.success(summary)
