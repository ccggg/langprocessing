from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem.porter import *
from nltk import word_tokenize
from nltk.tokenize import wordpunct_tokenize
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import re
import os
from io import open
import numpy as np

def normalised_string (input_string, lower_case=True):
    """
    :param input_string: str
    :param lower_case: boolean
    :rtype: str
    """
    if input_string is None:
        return ''
    normalised_text = ''
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = sent_detector.tokenize(input_string.strip())
    for sentence in sentences:
        tokens = wordpunct_tokenize(sentence)
        normalised_sentence = ''
        for token in tokens:
            if lower_case:
                normalised_sentence += str(token).lower()+' '
            else:
                normalised_sentence += str(token) + ' '
        normalised_sentence = str(normalised_sentence).strip()
        normalised_text += normalised_sentence+'\n'
    normalised_text = str(normalised_text).strip()
    return normalised_text

class StemTokenizer(object):
    def __init__(self, number_of_files=None):
        self.wnl = WordNetLemmatizer()
        self.number_of_files = number_of_files

    counter = 0

    def __call__(self, doc, remove_stop_words=True):

        """
        :param doc: string
        :param remove_stop_words: Boolean
        :return: List[String]
        """
        stop_pos_tags = ['CD', 'RB', 'CC', 'DT']

        if not remove_stop_words:
            return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]
        else:
            stemmer = PorterStemmer()
            lemmas = []
            tokenised_text = word_tokenize(doc)
            tagged_text = nltk.pos_tag(tokenised_text)
            for tag in tagged_text:
                if len(tag[0]) <= 1 or tag[1] in stop_pos_tags:
                    continue

                try:
                    if tag[0] in stopwords.words('english') or stemmer.stem(tag[0]) in stopwords.words('english'):
                        continue
                except (IndexError):
                    if tag[0] in stopwords.words('english'):
                        continue
                try:
                    lemmas.append(stemmer.stem(tag[0]))
                except (IndexError):
                    continue

            StemTokenizer.counter = StemTokenizer.counter + 1

            if self.number_of_files is None:
                print('done pre-processing file', StemTokenizer.counter)
            else:
                print('done pre-processing file', StemTokenizer.counter, ' / ', self.number_of_files)
            return lemmas


def get_bag_of_words(documents):

    clean_documents = []
    for document in documents:
        document = normalised_string(input_string=document)
        clean_documents.append(document)


    count_vectorizer = CountVectorizer(max_features=20000,
                                       min_df=1,
                                       stop_words='english',
                                       tokenizer=StemTokenizer(number_of_files=len(clean_documents)))
    bag_of_words = count_vectorizer.fit_transform(clean_documents)
    all_attribute_words = count_vectorizer.get_feature_names()
    return bag_of_words, all_attribute_words

if __name__ == '__main__':

    doc_dir = 'Z:/My Documents/Python/SciKit Learn/Test/keywords/'
    documents = []
    for file in os.listdir(doc_dir):
        with open(doc_dir + '/' + file, 'r', encoding='utf-8-sig') as open_file:
            for line in open_file:
                documents.append(line.strip())

    # an array of documents/reviews/scripts
    #documents = ['Scene: Centresssl Perk, Chandler, Joey, Phoebe, and Monica, Monica are there.',
                #'Scene: Monica\'s Apartment, everyone is there and watching a Spanish Soap on TV TV TV and are trying to figure out what is going on.',
                #'Scene: The Subway, Phoebe is singing for change.']

    # the bag_of_words holds the 0's or integer > 0 representation of the documents
    bag_of_words, all_attribute_words = get_bag_of_words(documents = documents)
    print all_attribute_words
    print documents[2]
    print bag_of_words[2]
