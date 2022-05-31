# Функции

# def a_function():
#     print('fasfasfsfacacsasdasdds')
#     pass
# a_function()
# a_function()

# import random
#
#
# def summa():
#     c = [random.randint(0, 5) for _ in range(10)]
#     print(c)
#     a = 0
#     for i in c:
#         a += i
#     print(a)
#
#
# summa()
# summa()


# def add(a, b):
#     return (a + b)
#
#
# total = add(a=3, b=25)
#
# print(total)
# print(add(2, 3))

# def add(a, b):
#     return (a + b)
#
#
#
#
# print(add)
# print(add(2, 3))

# def www(a, b=2, c=3):
#     return a + b + c
#
#
# # www(b=4, c=5)# выдаст ошибку
# print(www(1, b=4, c=5))
# print(www(1))


# def many(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# many(1, 2, 3, 5, 6, 4, 3, 2, 'yuuyggjhgjhgj',name='mike', job='programmer')


# def fun_a():
#     global a_gl
#     a_gl = 1
#     b = 2
#     return a_gl + b
#
#
# def fun_b():
#     c = 3
#     return a_gl + c
#
#
# print(fun_a())
# print(fun_b())

# def fun1(a, b):
#     def fun1_1(x):
#         return x * x * x
#
#     return fun1_1(a) + fun1_1(b)
#
#
# print(fun1(3, 5))


# def sum(a, b): return a + b
#
#
# print(sum(1, 8))


# задача
# def is_year_leap():
#     year = int(input('введите год  '))
#     if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#         print('високосный год')
#     else:
#         print('Не високосный год')
# is_year_leap()


def season(x):
    if 1 <= x <= 2 or x == 12:
        print('зима')
    elif 3 <= x <= 5:
        print('весна')
    elif 6 <= x <= 8:
        print('лето')
    else:
        print('осень')
    return x
print(season(int(input('введите номер месяца  '))))
