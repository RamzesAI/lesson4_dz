from itertools import count
from itertools import cycle
count_el = 0
my_list = [1, 45, 7]
print('---------------СКРИПТ 1-----------------')
for el in count(10):
    if el > 15:
        break
    else:
        print(el)

print('---------------СКРИПТ 2-----------------')
for el_c in cycle(my_list):
    if count_el > 5:
        break
    print(el_c)
    count_el +=1