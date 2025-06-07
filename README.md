# Movie Recommender System

A web application that recommends movies based on your preferences using content-based filtering. The application uses TMDB API to fetch movie posters and provides a user-friendly interface built with Streamlit.

## Features

- Movie recommendations based on content similarity
- Beautiful UI with movie posters
- Real-time movie data from TMDB
- Easy-to-use interface

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/movies-recommender-system.git
cd movies-recommender-system
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/Scripts/activate  # On Windows
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

The application will automatically download the required data files (movies.pkl and similarity.pkl) from Google Drive on first run.

## Data

The application uses two main data files:

- `movies.pkl`: Contains movie metadata
- `similarity.pkl`: Contains the similarity matrix for content-based filtering

These files are automatically downloaded from Google Drive when you first run the application.

## Technologies Used

- Python
- Streamlit
- Pandas
- TMDB API
- Google Drive API (via gdown)
