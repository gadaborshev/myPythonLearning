# Напишите программу, которая принимает первым аргументом командной строки полный автомобильный номер,
# а после выводит его регистрационный номер

import sys

full_number = sys.argv[1]
# full_number = 'с065мк78'
short_number = full_number[1:4]
print(short_number)