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

data_input = [ "Excellent movie.",
               "I loved the movie.",
               "The movie was pretty poor.",
               "Bad.",
               "Eh.",
               "The movie was great",
               "Could have been better.",
               "Fantastic.",
               "Not good.",
               "Best film I have ever seen.",
               "Nice."]

data_input_counts = movie_vec.transform(data_input)
data_input_tfidf = tfidf_transformer.transform(data_input_counts)

pred = clf.predict(data_input_tfidf)

for review, category in zip(data_input, pred):
    print review
    print "This is a", movie_train.target_names[category], "review."
    print ""
