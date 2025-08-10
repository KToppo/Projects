# 📚 Book Recommendation System

A **Streamlit-based** web application that recommends books to readers using **Popularity-Based** and **Collaborative Filtering** techniques.  
The project uses the **Book Recommendation Dataset** from Kaggle and leverages **Cosine Similarity** to generate personalized recommendations.

---

## 🚀 Features

- **Top 50 Books**  
  Displays the most popular books with average ratings (minimum 250 votes).

- **Personalized Recommendations**  
  Suggests similar books based on a selected title using collaborative filtering.

- **Interactive UI**  
  Built with Streamlit for smooth, responsive user interaction.

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **Frameworks/Libraries**:
  - [Streamlit](https://streamlit.io/) – Interactive UI
  - [Pandas](https://pandas.pydata.org/) – Data manipulation
  - [NumPy](https://numpy.org/) – Numerical computation
  - [scikit-learn](https://scikit-learn.org/) – Cosine similarity
  - [kagglehub](https://github.com/Kaggle/kagglehub) – Dataset download
  - [Pickle](https://docs.python.org/3/library/pickle.html) – Model persistence

- **Dataset**: [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) from Kaggle

---

## 📂 Project Structure

```plaintext
.
├── app.py                           # Streamlit web app
├── book-recommendation-system.ipynb # Data processing & model building
├── kaggle_handler.py                # Kaggle dataset download handler
├── top50books.pkl                   # Precomputed top 50 books
├── user_matrix.pkl                  # Pivot table (Book-Title x User-ID)
├── similarity.pkl                    # Cosine similarity scores
├── book_poster.pkl                   # Mapping of books to image URLs
└── Assets/                           # Dataset files
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/book-recommendation-system.git
cd book-recommendation-system
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```


### 3️⃣ Run the notebook to generate `.pkl` files
```bash
jupyter notebook book-recommendation-system.ipynb
```
This will:
- Download the dataset via **kaggle_handler.py**
- Preprocess data
- Generate `.pkl` files used by the web app

### 4️⃣ Start the Streamlit app
```bash
streamlit run app.py
```

---

## 🎯 How It Works

### 1. Popularity-Based Recommendation
- Filters books with more than **250 votes**
- Ranks them by **average rating**
- Displays top 50 results

### 2. Collaborative Filtering
- Creates a **User-Book rating matrix**
- Computes **cosine similarity** between books
- Suggests top 5 similar books for the selected title

---

## 🖼️ Screenshots

### 🔹 Top 50 Books
![Top 50](https://github.com/KToppo/Projects/blob/master/book_recomendation_system/assets/S2.png)

### 🔹 Recommendations
![Recommendations](https://github.com/KToppo/Projects/blob/master/book_recomendation_system/assets/S1.png)

---


## 🤝 Contributing

Contributions are welcome!  
- Fork the repo

---


## 📧 Contact

Created by **Kalyan Toppo**  
For questions or suggestions: [LinkedIn](https://www.linkedin.com/in/kalyantoppo/) | [GitHub](https://github.com/KToppo)
