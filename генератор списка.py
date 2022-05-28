# генератор списка
import random

c = [random.randint(0, 9) for i in range(10)]

print(c)
print(c[0], c[-1])

# генератор
import random
a = random.randint(110, 999) # int число
c = [random.randint(0, 5) for _ in range(10)] #список
с= tuple([random.randint(0, 5) for _ in range(10)]) # кортеж
d = {i: random.randint(1, 10) for i in ['a', 'b', 'c']} #cловарь
d = set([random.randint(1, 99) for i in range(10)]) # множество, но нужно учесть что дублирующие элементы не выводятся

# генератор словарей
import random
a = ['a', 'b', 'c']
d = {i: random.randint(1, 10) for i in a}

d = {a: a ** 2 for a in range(7)}