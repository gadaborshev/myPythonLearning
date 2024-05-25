import sys

number = sys.argv[1]
number = number.\
    replace("a", "0").\
    replace(" ", "1").\
    replace("b", "2").\
    replace("x", "3").\
    replace("lee", "8").\
    replace("mu", "5").\
    replace("n", "6").\
    replace("o", "7").\
    replace("l", "4").\
    replace("f", "9")
print(number)