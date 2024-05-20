import sys

word = sys.argv[1]

word_lower = word.lower()
word_upper = word.upper()
print(word, word_lower, word_upper, sep=", ")