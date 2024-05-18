# Без скобок сперва будет выполнено умножение b и c.
# А уже после к результату будут добавлены a и d.
# a + b * c + d

# Со скобками, сперва произойдет сложение a и b, с и d.
# А уже после будет перемножен результат.
# (a + b) * (c + d)

js_junior = 50000
js_middle = 80000
js_senior = 130000
python_junior = 60000
python_middle = 85000
python_senior = 120000

avg_salary = (js_junior + js_middle + js_senior + python_junior + python_middle + python_senior) / 6

print(avg_salary)