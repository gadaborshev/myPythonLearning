import sys

word = sys.argv[1]
# word = "Gadaborshev"

print("+" + ("-" + ("-" * len(word) + "-") + "+"))
print("|" + " " + word + " " + "|")
print("+" + ("-" + ("-" * len(word) + "-") + "+"))

# from teacher
# import sys
#
# word = sys.argv[1]
#
# # Вычисляем верхнюю и нижнюю линию.
# line = "+-" + "-" * len(word) + "-+"
#
# # Выводим линию, слово и линию.
# print(line)
# print("| " + word + " |")
# print(line)