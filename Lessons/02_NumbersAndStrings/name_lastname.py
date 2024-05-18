import sys

name = sys.argv[1]
lastname = sys.argv[2]

print(lastname, name[0], end='.')


import sys

# Получаем имя и фамилию.
first_name = sys.argv[1]
last_name = sys.argv[2]

# Склеиваем строку и выводим ответ.
# first_name[0] - первая буква имени
print(last_name + " " + first_name[0] + '.')

# Вариант 2 - форматирование строк (изучим далее)
print("{} {}.".format(last_name, first_name[0]))

# Вариант 3 (продвинутый) - f-строки, в курсе будет отдельный урок.
print(f"{last_name} {first_name[0]}.")