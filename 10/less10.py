# b = (1,)  # кортеж из 1 элемента
# a = (1, 2, 3, 4, 5)
# print(a, b)

# a = (1, 2, 3, 4, 5)
# b = [1, 2, 3, 4, 5]
# print(a.__sizeof__())
# print(b.__sizeof__())


#
# a=(0,1,2,3,4,5)
# print(a[0:3])
# print(a[:3])
# print(a[1:])
# print(a[0:3:2])
# print(a[::3])

# a=tuple() # Создание кортежа
# b=list() # создание списка
# print(a,b)

# a = (1, 2, 3, 4, 'abh', 5)
# a = list(a)
# print(a)
# a.append(72)
# print(a)
# a = tuple(a)
# print(a)

# a = (1, 2, 3, 4, 'abh', [1, 2, 3, 4], 5)
# a[5].append(77)
# print(a)
# print(a[0] + 10)

#
# a = (1, 2, 3, 4, 'abh', [1, 2, 3, 4], 5)
# b = (2, 44, 5, 6, 7)
# z = a + b
# print(z)
#
# v = a * 2  # к спискам тоже применяется
# print(v)

#
# a = (2, 44, 5, 6, 7)
# print(max(a)) #к спискам тоже применяется
# print(min(a)) #к спискам тоже применяется
# print(sum(a)) #к спискам тоже применяется

# a = ('jhdsf', 'gjh', 'husd', 'ss')
# print(max(a, key=len))  # к спискам тоже применяется
# print(min(a, key=len))  # к спискам тоже применяется
# for i in a:
#     print(i, len(i))


# a = ('asd', 'sd', 'asddas')
#
# print(max(a, key=len))  # к спискам тоже применяется
# print(min(a, key=len))  # к спискам тоже применяется
# for i in a:
#     print(i, len(i))
# ind_max = a.index(max(a, key=len))
# print(a[ind_max], len(a[ind_max]))


# генератор списка
# import random
# #вар1
# c = [random.randint(0, 1000) for i in range(10)]
#
# print(c)
# c = tuple(c)
# print(c)
# print(max(c))
# print(min(c))

# import random
#
# c = [random.randint(0, 5) for i in range(10)]
# b = [random.randint(-5, 0) for i in range(10)]
# print(c, b)
# c = tuple(c)
# b = tuple(b)
# print(c, b)
# z = c + b
# print(z)
# q = 0  # счетчик print(z.count(0))
# for i in z:
#     if i == 0:
#         q += 1
# print('количество 0:', q)
# print('end')

# import random
#
# c = tuple([random.randint(0, 100) for i in range(10)])
# print(c)

# a = ('sdsd', 'dsfdsf', 'sdf', 'ff', 'eeerw', 1, 2, 444)
# print(a)
#
# print(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7])
#
#
# a = ('sd', 'weriq', 'ggg', 1, 88)
# print(', '.join([str(i) for i in a]))

a = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
b = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
a1 = sum(a)
b1 = sum(b)
print(a1, b1)
if a1 > b1:
    print('сумма кортежа a>b ', a1, ">", b1)
elif b1 > a1:
    print('сумма кортежа b>a ', b1, ">", a1)
print('min а:', min(a), 'min b:', min(b))
print('порядковый номер min а:', a.index(min(a)) +1, 'порядковый номер min b:', b.index(min(b)) + 1)
