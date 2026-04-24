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
## Project Structure

```bash
movie-recommender-system/
│
├── Images/                  # Application screenshots
│
├── app.py                   # Streamlit application
│
├── movies_dict.pkl          # Movie metadata dictionary
├── similarity.pkl.gz        # Compressed similarity matrix
│
├── requirements.txt         # Project dependencies
│
├── README.md                # Documentation
│
├── .gitignore
└── .gitattributes
```
```

---

## Installation

```bash
git clone https://github.com/Mayurk906/movie-recommender-system.git
cd movie-recommender-system
pip install -r requirements.txt
streamlit run app.py
```

---

## Future Improvements
- Add TF-IDF vectorization
- Build hybrid recommender
- Add collaborative filtering
- Improve recommendation explainability
