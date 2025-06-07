# 🎬 Movie Recommender System

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)

---

<img src="https://img.icons8.com/color/96/000000/movie-projector.png" width="80" align="left" style="margin-right: 16px;"/>

## Welcome to the Movie Recommender System!

Get personalized movie recommendations based on your favorite film. This app uses content-based filtering and the TMDB API to fetch movie posters, all wrapped in a beautiful Streamlit interface.

---

## 🚀 Features

- 🎥 **Personalized Recommendations**: Get 5 movies similar to your favorite
- 🖼️ **Movie Posters**: See posters fetched live from TMDB
- ⚡ **Fast & Modern UI**: Responsive, dark-themed, and visually appealing
- 🗃️ **Efficient Data Handling**: Uses Git LFS for large files
- 🔒 **No API Key Needed for Users**: All handled in the backend

---

## 🛠️ Setup & Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Ashish-gaba/movie-recommender-system.git
   cd movie-recommender-system
   ```

2. **Install Git LFS (if not already):**

   ```bash
   git lfs install
   git lfs pull
   ```

3. **Create and activate a virtual environment:**

   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Mac/Linux:
   source .venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

The app will load the required data files (`movies.pkl` and `similarity.pkl`) automatically. If you fork or clone, make sure to run `git lfs pull` to fetch the data files.

---

## 📦 Data

- **movies.pkl**: Movie metadata
- **similarity.pkl**: Content similarity matrix

Both files are managed with Git LFS for efficient storage and versioning.

---

## 🧰 Technologies Used

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [TMDB API](https://www.themoviedb.org/documentation/api)
- [Git LFS](https://git-lfs.github.com/)

---

## 💡 Customization

- You can easily change the UI or recommendation logic in `app.py`.
- To use your own TMDB API key, update the `API_KEY` variable in the code.

---

## 📣 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is licensed under the MIT License.
