import streamlit as st
import fitz  # PyMuPDF
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load model and tokenizer
model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')

st.title("PDF Text Summarizer using T5 Transformer")

# File uploader for PDF
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# Process uploaded PDF
if pdf_file is not None:
    extracted_text = extract_text_from_pdf(pdf_file)
    st.subheader("Extracted Text")
    st.write(extracted_text[:2000])  # limit display to 2000 chars

    if st.button("Summarize"):
        input_text = "summarize: " + extracted_text
        inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

        summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        st.subheader("Summary:")
        st.write(summary)

