import sys

distance = sys.argv[1]
distance_str = "Расстояние: N км"

# Берем строку до N, добавляем к ней distance, а после строку после N.
distance_str = distance_str[:12] + distance + distance_str[13:]

print(distance_str)

#
# Альтернативный вариант через метод replace (пройдем немного позже)
#
print(distance_str.replace("N", distance))