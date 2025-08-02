
# 🎬 Movie Recommender System

This is a **Movie Recommender Web App** built using **Streamlit**. It recommends similar movies based on your selected movie using a content-based filtering model trained on movie metadata.

---

## 📂 Project Structure

```text
.
├── app.py                      # Streamlit application
├── movie-recommender-system.ipynb  # Jupyter notebook for model training and feature engineering
├── requirements.txt           # Required Python packages
├── movie_list.pkl             # Serialized movie metadata (download separately)
├── similarity.pkl             # Precomputed similarity matrix (download separately)
```

---

## 🧠 How It Works

- Uses content-based filtering to recommend movies.
- Movie metadata (like genres, keywords, cast, etc.) is used to calculate similarity between movies.
- When a user selects a movie, it finds the top 5 most similar movies and displays their posters using **TMDB API**.

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/KToppo/Projects/tree/master/movie_recommendation_system
   cd movie_recommendation_system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download required model files from Google Drive**  
   These files are too large to be stored in the GitHub repo:

   - [movie_list.pkl](https://drive.google.com/file/d/1T3fi5abR0guHNWET5T604NyPaDCRYREm/view?usp=sharing)
   - [similarity.pkl](https://drive.google.com/file/d/1ngcGIzRd7yaR-SoEehsq8FKJ95G9_LjI/view?usp=sharing)

   After downloading, place both files in the root directory of the project (same folder as `app.py`).

4. **Add your TMDB API key**
   - Replace `API_KEY = None` in `app.py` with your actual API key from [TMDB](https://www.themoviedb.org/)
   - Example:
     ```python
     API_KEY = "your_tmdb_api_key"
     headers["Authorization"] = f"Bearer {API Read Access Token}"
     ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

---

## 🧪 Model Training

You can find the complete model training and data preparation pipeline in the notebook:

- `movie-recommender-system.ipynb`

It includes:
- Data cleaning
- Feature engineering
- Vectorization (using CountVectorizer)
- Cosine similarity computation

---

## 🌐 API Usage

This project uses [TMDB API](https://developers.themoviedb.org/3) to fetch high-quality movie posters.

---

## 📷 Sample Output

> Once you run the app, you’ll see a dropdown of movie titles and, on clicking "Recommend", the app displays similar movies with their posters side-by-side.

---

## 🙋‍♂️ Author

**Kalyan Toppo**

> Feel free to connect on [LinkedIn](https://www.linkedin.com/in/kalyantoppo/) or contribute to the project via pull requests.
