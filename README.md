# 🎬 Movie Recommendation System

This is a **Content-Based Movie Recommendation System** that uses **Natural Language Processing (NLP)**, specifically the **Bag-of-Words (BoW)** model, to recommend movies similar to the one entered by the user. The application is built with **Streamlit** for an interactive web interface.

---

## 🚀 Features

- Recommend movies similar to the one you input.
- Based on **content-based filtering** using movie metadata (genres, keywords, cast, director, etc.).
- Utilizes **Bag-of-Words** for text vectorization.
- Clean and simple **Streamlit web interface**.

---

## 📚 How It Works

1. **Dataset**: The system uses a dataset containing movie metadata.
2. **Text Preprocessing**: Metadata such as title, genre, director, cast, and keywords are combined and preprocessed.
3. **Vectorization**: Bag-of-Words is used to convert text data into vectors.
4. **Similarity Measurement**: Cosine similarity is used to compare the vector of the input movie with all other movies.
5. **Recommendation**: The top 5 most similar movies are displayed.


## 🛠️ Tech Stack

- **Python**
- **Pandas**, **NumPy** – Data manipulation
- **Scikit-learn** – NLP and machine learning (`CountVectorizer`, `CosineSimilarity`)
- **Streamlit** – Web interface

---
