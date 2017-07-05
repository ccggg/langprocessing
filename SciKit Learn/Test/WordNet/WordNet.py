# https://pythonprogramming.net/wordnet-nltk-tutorial/

import os
import nltk
import linecache

from io import open
from nltk.tag import pos_tag
from nltk.corpus import wordnet as wn

file_dir = 'Z:/My Documents/Python/SciKit Learn/Test/keywords/keywords.txt'
with open(file_dir, 'r', encoding='utf-8-sig') as open_file:
        lines = open_file.readlines()
        line = lines[81]
        print line

        people = []

        for i in range(0, len(line.split())):
            word = line.split()[i]
            word = word.replace(',', '')
            word = word.replace('.', '')
            word = word.replace("'", '')
            word = word.replace("'s", '')
            print word
            #word_type = pos_tag(word.split())
            #print word_type

            try:
                syn = wn.synsets(word.split()[0])[0]
                if syn.lexname() == 'noun.quantity':
                    syn = wn.synsets(word.split()[0])[1]
            except IndexError:
                print 'Nothing returned'
                print ''
            else:
                print syn

                try:
                    hyp = syn.hypernyms()[0]
                    print 'Hypernym: ' + str(hyp)

                    while hyp:
                        hyp = hyp.hypernyms()[0]
                        print 'Hypernym: ' + str(hyp)

                except IndexError:
                    print '-----------------'
                    print 'No more Hypernyms'
                    print '-----------------'


                print 'Lexname: ' + str(syn.lexname())
                if syn.lexname() == 'noun.person':
                    if word not in people:
                        people.append(word)

                print 'Lemmas: ' + str(syn.lemma_names())
                print ''
        print people
