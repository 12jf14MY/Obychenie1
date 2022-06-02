# Рекурсия
# факториал n!=n*n-1*n-2*...2*1
# def factorial(n):
#     if n != 0:
#         return n * factorial(n - 1)
#     else:
#         return 1
#
#
# print(factorial(6))


# def func(x):
#     return x
# a1=func
# a2=a1
# print(a2(10))


# a = lambda x, y: x * y
# print(a(2, 3))
# print(type)

# a = lambda x=1, y=2: x ** y
# sq = a
# print(a(5))

# def mul(a):
#     def helper(b):
#         return a * b
#
#     return helper
#
#
# print(mul(3)(2))
#
# mul_1=mul(3)  # a всегда будет 3 под привоенной переменной mul_1
# print(mul_1(5)) #  значению b даем аргумент 5


# Декоратор функции
# def first_test():
#     print('Test function 1')
#
#
# def second_test():
#     print('Test function 2')
#
#
# def ssss(fn):
#     def apper():
#         print('start function')
#         fn()
#         print('stop function')
#
#     return apper
#
#
# a = ssss(first_test)
# b = ssss(second_test)
# a() # вызов функции
# b() # вызов функции

# Либо

# def ssss(fn):
#     def apper():
#         print('start function')
#         fn()
#         print('stop function')
#
#     return apper
#
# @ssss
# def first_test():
#     print('Test function 1')
#
#
# @ssss
# def second_test():
#     print('Test function 2')
#
# first_test()
# second_test()

# def param(fn):
#     def wrapper(arg):
#         print('Start function:' + str(fn.__name__) + '(), with param:' + str(arg))
#         fn(arg)
#
#     return wrapper


# @param
# def pr(num):
#     print(num ** 0.5)
#
#
# pr(4)


# def fun(w):
#     print('разряд числа', len(w))
#
# fun(input('введите число  '))


# def digits(n):
#     i = 0
#     while n > 0:
#         n = n // 10
#         i += 1
#     return i
#
#
# num = int(input('Введите число: '))
# print('Количество разрядов:', digits(num))


def digits(n):
    return len(str(n))


num = int(input('Введите число: '))
print('Количество разрядов:', digits(num))





# a = []
#
#
# def f(*args, **kwargs):
#     for i in args:
#         if args.index(i) % 2 != 0:
#             print(args.index(i), '-', i)
#             a.append(i)
#     for value in kwargs.values():
#         if type(value) is str:
#             print(value)
#             a.append(value)
#     return a
#
# print(f(1, 2, 3, 4, n='Name', c='Belarus', num=123))





