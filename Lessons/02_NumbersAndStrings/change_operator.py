import sys

# Не меняйте строки ниже.
# code = sys.argv[1]
code = 926
phone = "+7 (951) 783-13-14"

# Исправьте код так, чтобы код 951 в строке phone был заменен на значение
# из переменной code.
phone = phone[:4] + code + phone[7:]

# Вывод нового номера.
print(phone)