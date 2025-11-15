import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration

st.title("Free Summarizer (No API Key)")

@st.cache_resource
def load_model():
    model = T5ForConditionalGeneration.from_pretrained("t5-small")
    tokenizer = T5Tokenizer.from_pretrained("t5-small")
    return model, tokenizer

model, tokenizer = load_model()

source_text = st.text_area("Enter text:", height=250)

if st.button("Summarize"):
    if not source_text.strip():
        st.error("Please enter text first.")
    else:
        input_text = "summarize: " + source_text
        inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

        summary_ids = model.generate(
            inputs,
            max_length=150,
            min_length=40,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )

        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        st.success(summary)
