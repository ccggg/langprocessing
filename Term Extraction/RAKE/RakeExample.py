# https://www.airpair.com/nlp/keyword-extraction-tutorial

from __future__ import absolute_import
from __future__ import print_function
import six

import Rake as rake
import operator
import io

# https://en.wikipedia.org/wiki/Stop_words
stoppath = "SmartStoplist.txt"

# Stop words, min characters, min words in phrase, min times word appears in text
rake_object = rake.Rake(stoppath)

# Body of text
text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility " \
       "of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. " \
       "Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating"\
       " sets of solutions for all types of systems are given. These criteria and the corresponding algorithms " \
       "for constructing a minimal supporting set of solutions can be used in solving all the considered types of " \
       "systems and systems of mixed types."


# Split the text into sentences
sentenceList = rake.split_sentences(text)

stopwordpattern = rake.build_stop_word_regex(stoppath)

phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern, rake.load_stop_words(stoppath), 4)

wordscores = rake.calculate_word_scores(phraseList)

keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)

sortedKeywords = sorted(six.iteritems(keywordcandidates), key=operator.itemgetter(1), reverse=True)
totalKeywords = len(sortedKeywords)

for keyword in sortedKeywords[0:(totalKeywords // 3)]:
    print("Keyword: ", keyword[0], " | Score: ", keyword[1])
