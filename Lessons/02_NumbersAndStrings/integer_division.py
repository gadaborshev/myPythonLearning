# Напишите программу, которая получает из первого аргумента командной строки число,
# а затем выводит два значения: целую часть от деления числа на 2 и остаток от деления числа на 2.
# Оба значения нужно вывести в одной строке.

import sys

# Получаем целое число из первого аргумента командной строки.
# Обратите внимание, что через аргументы командной строки мы всегда передаем и принимаем строки,
# поэтому нам нужно применять функцию int(), чтобы сделать из них числа.

# number = int(sys.argv[1])

number = 33

# Напишите ваш код тут.
whole_part = int(number // 2)
modulo = int(number % 2)

print(whole_part, modulo)