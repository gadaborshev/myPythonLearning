# Напишите программу, которая получает первым аргументом командной строки текст, а после обрезает его до 10 символов
# и добавляет в конец три точки.

import sys

text = sys.argv[1]
# text = "I'm good programmer"
print(text[0:10] + "...")