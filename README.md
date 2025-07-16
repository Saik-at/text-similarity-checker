# AI-Generated Text Similarity Checker

A web-based tool that uses Sentence Transformers to calculate the semantic similarity between two pieces of text. Ideal for plagiarism detection, paraphrasing evaluation, or GenAI output comparisons.

---

## Features

- Accepts two user-provided text inputs
- Uses `all-MiniLM-L6-v2` model from Sentence Transformers
- Computes cosine similarity score in real time
- Streamlit UI for interactive testing

---

## Project Structure

text_similarity_checker/
├── streamapp.py # Streamlit UI
├── similarity.py # Logic for generating embeddings and computing similarity
├── requirements.txt # Dependencies


---

## ⚙️ Installation

Install the required libraries:

Copy and paste this in terminal:
pip install -r requirements.txt

## Run the App

Copy and paste this in terminal:
streamlit run streamapp.py

This automatically opens the link in your browser (usually http://localhost:8501)

## Model Used
all-MiniLM-L6-v2

This model converts input text into 384-dimensional embeddings optimized for sentence-level similarity tasks.

## Author
Saikat Jana
GitHub: Saik-at

## License
This project is open-source under the MIT License.


