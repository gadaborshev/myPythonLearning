import sys

phrase = sys.argv[1]

phrase = phrase.\
    replace("I am",  "I'm").\
    replace("You are", "You're").\
    replace("He is", "He's").\
    replace("She is", "She's").\
    replace("It is",  "It's").\
    replace("We are", "We're").\
    replace("They are", "They're")
print(phrase)