card_number = "4563123483405831"
print(card_number[:8])
hidden_card_number = "*" * 12 + card_number[-4:]
print(hidden_card_number)
# print(card_number[0:4])  # [0:4] = [0, 1, 2 3], не захватывая индекс 4
#
# print(card_number[12:15])  # [12:15] = [12, 13, 14] 15 - срез не затрагивает позицию 15
#
# # Если ты хочешь захватить символ с индексом 15, тебе нужно сделать конечный индекс 16,
# # так как он не включается в срез
# print(card_number[12:16])
#
# # а можно предыдущую строку написать и так, и этот подход гораздо гибче
# print(card_number[12:len(card_number)])
#
# # и так
# print(card_number[-4:len(card_number)])
#
# # и так
# print(card_number[-4:])