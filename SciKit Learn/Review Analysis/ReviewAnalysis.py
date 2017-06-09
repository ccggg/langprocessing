# http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html#tutorial-setup

import nltk
from sklearn.datasets import load_files
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# Directory of the dataset
filedir = r'G:\Python\DataSets\movie_reviews'

# Load the dataset from the file diretory to be used as training data
movie_train = load_files(filedir, shuffle=True)

movie_vec = CountVectorizer(min_df=2, tokenizer=nltk.word_tokenize)
movie_counts = movie_vec.fit_transform(movie_train.data)

tfidf_transformer = TfidfTransformer()
movie_tfidf = tfidf_transformer.fit_transform(movie_counts)
docs_train, docs_test, y_train, y_test = train_test_split(movie_tfidf, movie_train.target, test_size = 0.20, random_state = 12)

clf = MultinomialNB().fit(docs_train, y_train)

reviews_new = ["This movie was excellent.",
               "Absolute joy ride.",
               "The movie was pretty poor.",
               ""]

reviews_new_counts = movie_vec.transform(reviews_new)
reviews_new_tfidf = tfidf_transformer.transform(reviews_new_counts)

pred = clf.predict(reviews_new_tfidf)

for review, category in zip(reviews_new, pred):
    print('%r => %s' % (review, movie_train.target_names[category]))
