# Hybrid Movie Recommendation System

## Overview
This project is a content-based movie recommendation system that suggests similar movies using Natural Language Processing (NLP) and cosine similarity.

Users enter a movie name, and the system recommends top similar movies based on metadata such as genres, keywords, cast, and crew.

---

## Features
- Content-based recommendation engine
- Top 5 similar movie recommendations
- Metadata-driven similarity matching
- Streamlit interactive web app

---

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit

---

## Dataset
TMDB 5000 Movies Dataset

---

## Methodology
1. Data preprocessing  
2. Feature engineering  
3. Text vectorization using CountVectorizer  
4. Cosine similarity computation  
5. Recommendation generation

---

## Project Structure

```bash
movie-recommender-system/
│
├── data/
├── src/
├── app.py
├── similarity.pkl
├── movie_dict.pkl
├── requirements.txt
└── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Future Improvements
- Add TF-IDF vectorization
- Build hybrid recommender
- Add collaborative filtering
- Improve recommendation explainability
