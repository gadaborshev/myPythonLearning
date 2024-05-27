import sys

phrase = sys.argv[1]

# phrase = '<p>текст</p><h1>Заголовок</h1><p>еще текст</p>'

h1_start_position = phrase.find('<h1>') + 4
h1_end_position = phrase.find('</h1>')

h1 = phrase[h1_start_position:h1_end_position]

print(h1)


