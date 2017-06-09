# http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html#tutorial-setup

import numpy as np

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Take four of the twenty available datasets for faster execution time.
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']

# The list of files matching the defined categories can now be loaded.
twenty_train = fetch_20newsgroups(subset = 'train', categories=categories, shuffle=True, random_state=42)

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print count_vect.vocabulary_.get(u'algorithm')

tfidf_transformer  = TfidfTransformer()
X_train_tfidf  = tfidf_transformer.fit_transform(X_train_counts)
print X_train_tfidf.shape

clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
docs_new = ['God is love', 'OpenGL']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
    print '%r => %s' % (doc, twenty_train.target_names[category])

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB())])

text_clf = text_clf.fit(twenty_train.data,
                        twenty_train.target)
