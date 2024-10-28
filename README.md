# Movie Recommendation System

This project is a Content-Based Movie Recommendation System that uses movie metadata from the TMDB 5000 dataset to recommend movies similar to a given title. The recommendation engine is built using techniques such as text preprocessing, stemming, and cosine similarity.

## Dataset

The dataset used for this project includes:
- `tmdb_5000_movies.csv`: Contains various details about movies like genres, keywords, overview, etc.
- `tmdb_5000_credits.csv`: Includes information about the cast and crew.

## Project Workflow

1. **Data Preprocessing**:
   - Merged the `movies` and `credits` datasets on the `id` column to create a single DataFrame (`new_movies`).
   - Dropped unnecessary columns, keeping only the ones relevant for recommendations (`id`, `original_title`, `genres`, `keywords`, `cast`, `crew`, `overview`).

2. **Feature Engineering**:
   - Combined `overview`, `genres`, `keywords`, `cast`, and `crew` columns into a single `tags` column, which serves as the main input for the recommendation model.
   - Used the following steps to populate the `tags` column:
     - Extracted genres, keywords, and cast/crew names as lists.
     - Limited the cast to the top three actors and extracted only the director’s name.
     - Removed spaces in multi-word names to avoid confusion during training.

3. **Text Vectorization**:
   - Transformed the `tags` column into a matrix of token counts using the `CountVectorizer` with a maximum of 5000 features and English stop words removed.
   - Applied stemming using NLTK's `PorterStemmer` to reduce similar words to their root form.

4. **Cosine Similarity Calculation**:
   - Calculated cosine similarity between all movies based on the vectorized `tags`, allowing us to measure the similarity between movies.

5. **Recommendation Function**:
   - Built a `recommend()` function that, given a movie title, retrieves the top 5 most similar movies based on cosine similarity.

6. **Saving Model and Data**:
   - Used the `pickle` library to save the processed movie details and similarity matrix for easy reuse.

## Example Usage

The project includes an example for generating recommendations. To use the recommendation function, load the `movie_list.pkl` and `similarity.pkl` files and call `recommend()` with a movie title:

```python
import pickle

# Load files
movies_df = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Example: Recommend movies similar to "Baby's Day Out"
recommend("Baby's Day Out")
```

## Project Setup

1. Install the required libraries:
   ```bash
   pip install numpy pandas matplotlib seaborn sklearn nltk
   ```
2. Download `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` datasets.
3. Run the notebook or script provided to process data, train the model, and generate recommendations.

## Dependencies

- **Python 3.x**
- **Libraries**: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `nltk`, `pickle`

## Acknowledgements

Data used in this project is from [The Movie Database (TMDB)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
