# elements = [1, 3, 'a', 6, 'b']
# elements = list()
# print(elements


# генератор списка
# import random
# c = [random.randint(0, 9) for i in range(10)]
# print(c[0], c[-1])
# c.append(777)
# print(c)


# l = [12, 654, 'reare', 456, 13, 13, 33]
# l.insert(2, 'ffff')  # вставляем fff на 2 позицию
# l.insert(4, 'hello')
# print(l)
#
# # если нужно заменить
# l[5] = 'good'
# print(l)

# если нужно удалить из списка
# l = [12, 654, 'reare', 456, 13, 13, 33]
# del l[2]
# print(l)
# del l[2:4]
# print(l)
#
# # удалить по названию
#
# l.remove(654)
# print(l)


# l = [12, 654, '25', 456, 13, 13, 33]
# print(12 in l)
# if 12 in l:
#     print('yes')


# дополняем список

# l = [12, 654, '25', 456, 13, 13, 33]
# b = [12,45,5,6]
# print(l+b)
# c=l+b
# print(c)


# l = [12, 654, '25', 456, 13, 13, 33]
# d = [45, 5, 6]
# d.extend(l)  # дополняем d
# print(d)

# a = [1, 2, 3, 'aa']
# b = a  # ссылка на список
# b.append(77)
# a.append(66)
# print(a, b)
#
# print(id(a), id(b))
# c = a.copy()
# c.append(44)
# print(c)
# print(id(a), id(c))


# # различие  способы при помощи for и while
# a = [1, 2, 3, 4]
# for i in a:
#     print(i)
#
# print('-' * 20)
#
# b = [1, 2, 3, 4, 5]
# b_l = len(b)
# i = 0
# while i < b_l:
#     print(b[i])
#     i = i + 1  # i+=1


# b.pop() удаляет индекс по списку


a = [1, 2, 3, 4]
a.clear()
print(a)

b = [0, 1, 1, 2, 3, 4]
print('колич повторений числа 1:', b.count(1), 'insex элемента 4:', b.index(4))
x = b.pop(4)
print(b)
print(x)
b.reverse()
print(b)


# сортировка по возрастанию и убыванию

# b = [1, 45, 78, 5, 2, 3, 7, 8, 0]
# b.sort()
# print(b)
# b.sort(reverse=True)  # сортировка в обратном порядке
# print(b)
#
# s = ['sdff', 'sdfsgg', 'ddd', 'd','er']
# s.sort()
# print(s)
# s.sort(key=len) # сортировка по количеству символов
# print(s)


# a = [1, 2, 5, 7, 'erw', [2, 3, 7]]
# print(a[5], [-1])
# # аналог
# b = a[5]
# print(b)
# print(b[-1])


# import random
#
# c = [random.randint(0, 10) for i in range(20)]
# print(c)
# c.reverse()
# print(c)
# c.sort(reverse=True)
# print(c)

# s = [1, 5, 78, 456, 52, 2, 20, 56, 789, 41, 5, 2, 3, 4]
# a = s.index(20)
# print(a)
# s[a] = 200
# print(s)
