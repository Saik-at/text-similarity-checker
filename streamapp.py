import streamlit as st
from utils import compute_similarity

st.set_page_config(page_title="Text Similarity Checker", layout="centered")

st.title("AI-Generated Text Similarity Checker")
st.write("Compare two texts and find out how semantically similar they are.")

# Input fields
text1 = st.text_area("Enter first text:")
text2 = st.text_area("Enter second text:")

# When button is clicked
if st.button("Compare"):
    if text1.strip() and text2.strip():
        score = compute_similarity(text1, text2)
        st.success(f"Similarity Score: **{score}%**")
    else:
        st.warning("Please enter text in both fields.")
