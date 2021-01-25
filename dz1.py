from sys import argv
script_name, production_in_hour, pay_for_hour, prize = argv
print('Файл для расчета: ', script_name)
print('Выработка в часах: ', production_in_hour)
print('Ставка в час: ', pay_for_hour)
print('Премия: ', prize)
print('Зарплата составит: ', (int(production_in_hour) * int(pay_for_hour)) + int(prize))

#запуск в командной строке из папки с файлом: python dz1.py 100 200 300