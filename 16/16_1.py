# Дан список. Выведите те его элементы, которые встречаются в списке только один
# раз. Элементы нужно выводить в том порядке, в котором они встречаются в
# списке.

import random

c = [random.randint(0, 9) for i in range(20)]
print(c)
c1 = []
for i in c:
    a = c.count(i)
    if a == 1:
        c1.append(i)
print(c1)
