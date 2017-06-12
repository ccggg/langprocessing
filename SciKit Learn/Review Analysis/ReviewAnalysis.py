# http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html#tutorial-setup

import nltk
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_files
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# Directory of the dataset
filedir = r'G:\Python\DataSets\movie_reviews'

# Load the dataset from the file diretory to be used as training data
movie_train = load_files(filedir, shuffle = True, random_state = 19)

# Convert a collection of text documents to a matrix of token counts
movie_vec = CountVectorizer(min_df = 2, tokenizer = nltk.word_tokenize)
movie_counts = movie_vec.fit_transform(movie_train.data)

tfidf_transformer = TfidfTransformer()
movie_tfidf = tfidf_transformer.fit_transform(movie_counts)

clf = MultinomialNB().fit(movie_tfidf, movie_train.target)

reviews_new = ["It was a decent movie.",
               "I loved the movie.",
               "The movie was pretty poor.",
               "Bad.",
               "Eh.",
               "Could have been better.",
               "Good.",
               "Not good.",
               "Best film I have ever seen.",
               "4/10",
               "7/10",
               "Nice."]

reviews_new_counts = movie_vec.transform(reviews_new)
reviews_new_tfidf = tfidf_transformer.transform(reviews_new_counts)

pred = clf.predict(reviews_new_tfidf)

for review, category in zip(reviews_new, pred):
    print review
    print "This is a", movie_train.target_names[category], "review."
    print ""
