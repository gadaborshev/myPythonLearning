# Напишите программу, которая получает 4 целых числа (координаты точек), а затем рассчитывает и выводит расстояние между
# двумя точками используя формулу выше.
# Точки в программу передаются в следующем порядке: x1, y1, x2, y2.

import sys

# x1 = int(sys.argv[1])
# y1 = int(sys.argv[2])
# x2 = int(sys.argv[3])
# y2 = int(sys.argv[4])

x1 = -1
x2 = 3
y1 = 6
y2 = 2

# Напишите ваш код тут.
r = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(r)