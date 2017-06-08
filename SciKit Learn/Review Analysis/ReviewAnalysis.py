# http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html#tutorial-setup

from sklearn.datasets import load_files

filedir = r'G:\Python\DataSets\movie_reviews'

movie_train = load_files(filedir, shuffle=True)

print len(movie_train.data)
