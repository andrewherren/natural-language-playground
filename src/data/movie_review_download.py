"""This file loads the movie review corpus for NLP analysis

The corpus is hosted on nltk but originates from:
http://www.cs.cornell.edu/people/pabo/movie-review-data/
"""

import nltk
nltk.download("movie_reviews")
from nltk.corpus import movie_reviews

# documents = [(list(movie_reviews.words(fileid)), category)
#              for category in movie_reviews.categories()
#              for fileid in movie_reviews.fileids(category)]