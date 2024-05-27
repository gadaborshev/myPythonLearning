import sys

# Получаем сумму из аргумента командной строки
amount = sys.argv[1]

# Находим позицию точки
dot_position = amount.find('.')

# Извлекаем часть строки до точки
rubles = amount[:dot_position]

# Выводим результат
print(rubles)