# for i in range(4):
#     print(i)
#     print('hi')


# for i in range(1, 10, 2):
#     print(i)
# # print('hi')
# a = 10
# b = 0
# c = -1
#
# for i in range(a, b, c):
#     print(i, end='+')

# a = 'Я учу Python'
# for i in a:
#     print(i, end='___')
#     if i == 'у':
#         print('умка')
# print('результат')

# Необходимо вывести числа от 1 до 15 в порядке убывания.

# for i in range(15, 0, -1):
#     print(i, end=' _')


# a = 'я учу PYTHON python'
# b = ''
# for i in a:
#     if i.isupper():
#         print(b)
#         b = b + i
# print('результат', b)
#

# a = input("введите строку 'Я учу программирование' ")
# b = input("введите строку 'o' ")
# c = ""
# for i in a:
#     print(i, end=' ')
#     if i != b:
#         c = c + i
# print(c)
# print('конец')

# a = int(input("введите начальное число: "))
# b = int(input("введите конечное число: "))
# c = int(input("введите шаг: "))
# for i in range(a, b, c):
#     print(i, end=' ')
# print('конец')

# a = [1, 45, 7, 89, 45, 2]
# a_s = ['sdv', 'asdasd', 'asdsas']
# print(a, len(a))
# print(a_s, len(a_s))
# for i in a:
#     if i == 89:
#         #  break
#         continue
#     print(i, end=" ")
# print('готово')

a = [1, 2, 4, 6, 8, 9, 0]
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)
print(b)

a = [1, 2, 3]
c = 0
for i in a:
    print(c)
    c = c + i
print('Результат: ', c)

a = [1, 2, 3]
c = 1
for i in a:
    print(c)
    c = c * i
print('Результат: ', c)
