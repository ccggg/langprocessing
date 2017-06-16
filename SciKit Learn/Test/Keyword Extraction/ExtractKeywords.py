# https://pdfs.semanticscholar.org/5a58/00deb6461b3d022c8465e5286908de9f8d4e.pdf

import Rake as rake

import nltk
#nltk.download()
from nltk.tag import pos_tag

# https://docs.python.org/2/library/operator.html
import operator
from io import open

# https://pythonhosted.org/six/
import six

import os

# https://en.wikipedia.org/wiki/Stop_words
stopPath = "SmartStoplist.txt"

# Stop words, min characters, min words in phrase, min times word appears in text
rake_object = rake.Rake(stopPath)

file_dir = 'Z:/My Documents/Python/SciKit Learn/Test/scenes'
for file in os.listdir(file_dir):
    with open(file_dir + '/' + file, 'r', encoding='utf-8-sig') as open_file:
        for line_terminated in open_file:
            line = line_terminated.rstrip('\n').lower()
            print 'Old > ' + line
            #sentence = open_file.readlines()
            # Split the text into 'sentences', searches for punctuation which would end a 'sentence' (.!?:;, etc)
            sentenceList = rake.split_sentences(line)
            #print(sentenceList)

            # Generate the candidate keywords from the sentence list using the SmartStopList
            stopwordPattern = rake.build_stop_word_regex(stopPath)
            phraseList = rake.generate_candidate_keywords(sentenceList, stopwordPattern)

            # Calculate the word scores of the candidate keywords
            wordScores = rake.calculate_word_scores(phraseList)

            # Generate the candidate keyword scores
            keywordCandidates = rake.generate_candidate_keyword_scores(phraseList, wordScores)

            # Sort candidates by score to determine top-scoring keywords
            sortedKeywords = sorted(six.iteritems(keywordCandidates), key = operator.itemgetter(1), reverse = True)
            totalKeywords = len(sortedKeywords)

            word_list = []
            for keyword in sortedKeywords[0:(totalKeywords)]:
                word_list.append(keyword[0].lower())
                #print word_list

            new_word_list = [words for segments in word_list for words in segments.split()]

            print 'Key words/phrases > ' + str(word_list)
            print 'New > ' + ' '.join([i for i in line.split() if any(w in i.lower() for w in new_word_list)])
            print ''

        print ''


# Other Resources
# Topic Modelling - https://en.wikipedia.org/wiki/Topic_model
# LDA - https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation
