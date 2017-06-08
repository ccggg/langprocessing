# https://pdfs.semanticscholar.org/5a58/00deb6461b3d022c8465e5286908de9f8d4e.pdf

import Rake as rake

import nltk
#nltk.download()
from nltk.tag import pos_tag

# https://docs.python.org/2/library/operator.html
import operator

# https://pythonhosted.org/six/
import six

# https://en.wikipedia.org/wiki/Stop_words
stopPath = "SmartStoplist.txt"

# Stop words, min characters, min words in phrase, min times word appears in text
rake_object = rake.Rake(stopPath)

# Text which they keywords will be selected from
text = ""

# Take input from a user for the text string
text = raw_input("Enter a string: ")

# Split the text into 'sentences', searches for punctuation which would end a 'sentence' (.!?:;, etc)
sentenceList = rake.split_sentences(text)
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

# Display all the keywords along with their scores
for keyword in sortedKeywords[0:(totalKeywords)]:
    print "Keyword: ", keyword[0],
    print " |  Score: ", keyword[1]

    # https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    # Use NLTK to create a tag for each keyword (Verb, Adjective, Noun, etc)
    # JJ - Adjective, DT - Determiner, NN - Noun, VB - Verb
    tagged_sent = pos_tag(keyword[0].split())
    print tagged_sent

# Other Resources
# Topic Modelling - https://en.wikipedia.org/wiki/Topic_model
# LDA - https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation
