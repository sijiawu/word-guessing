#using https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt
#use the second parameter for itertools.permutations to specify numbers of letters to choose from
import itertools
import sys
input = sys.stdin.read().split()


with open("words_alpha.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

def is_english_word(word):
    return word.lower() in english_words

printed = []

for x in itertools.permutations(input):
    currentWord = ''.join(x)
    is_not_printed = not currentWord in printed 
    if(is_english_word(currentWord) and is_not_printed):
    	print currentWord
    	printed.append(currentWord)