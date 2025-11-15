import streamlit as st
import re

st.title("Free Summarizer (No API, No External Libraries)")

def summarize_text(text, num_sentences=3):
    # Split into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)

    # Score sentences by length & keyword frequency
    word_freq = {}
    for word in re.findall(r'\w+', text.lower()):
        if len(word) > 3:
            word_freq[word] = word_freq.get(word, 0) + 1

    sentence_scores = []
    for sentence in sentences:
        score = 0
        for word in word_freq:
            if word in sentence.lower():
                score += word_freq[word]
        sentence_scores.append((sentence, score))

    # Sort by score
    ranked_sentences = sorted(sentence_scores, key=lambda x: x[1], reverse=True)

    # Return top sentences
    summary = " ".join([s[0] for s in ranked_sentences[:num_sentences]])
    return summary


text = st.text_area("Enter text to summarize:", height=300)

if st.button("Summarize"):
    if not text.strip():
        st.error("Please enter some text.")
    else:
        summary = summarize_text(text, num_sentences=3)

        st.subheader("Summary:")
        st.success(summary)
