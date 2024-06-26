# Напишите программу, которая получает из аргументов командной строки 2 числа: рост в сантиметрах, и  вес в килограммах.
# Программа должна расчитывать индекс массы тела и вывести результат на экран.

import sys

# Получаем рост и сразу приводим к целому числу
h = int(sys.argv[1])

# Получаем массу и сразу приводим к целому числу
m = int(sys.argv[2])

# Преобразуем рост из сантиметров в метры
h_m = h / 100

# Рассчитываем индекс массы тела (BMI)
bmi = m / (h_m ** 2)

# Выводим результат
print(bmi)