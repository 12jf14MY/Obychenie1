# Функции

# def a_function():
#     print('fasfasfsfacacsasdasdds')
#     pass
# a_function()
# a_function()

import random

def summa():
    c = [random.randint(0, 5) for _ in range(10)]
    print(c)
    a = 0
    for i in c:
        a += i
    print(a)
summa()
summa()
