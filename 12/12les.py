# множества

# a = {1, 9, 15, 4, 5, 'q', 'sdfsf', 234, 33, 'ds', 9, 9, 5, 4}
# print(a) # не учитывает дубликаты, дублирующие элементы удаляются
# print(len(a)) # выводит длину без дуликатов


# a = [1, 9, 15, 4, 5, 'q', 'sdfsf', 234, 33, 'ds', 9, 9, 5, 4]
# print(a)
# c = set()  # Создание множества
# c1 = set(a)
# print(c1, len(c1))
# a1 = list(c1)
# print(a1)

# a = {1, 9, 15, 4, 5, 'q', 'sdfsf', 234, 33, 'ds', 9, 9, 5, 4}
# for i in a:
#     print(i)
# print(1 in a)


# a = {1, 9, 15, 4, 5, 'q', 'sdfsf', 234, 33, 'ds', 9, 9, 5, 4}
# # a.discard(
# #     5)  # удаление элемента множества, если есть ошибка т.е. нет элемента во множестве но прога продолжает работать
# # a.remove(9)  # удаление элемента множества, но выдает ошибку и завершает работу
# # print(a)
# x = a.pop(9)
# print(x)

# x = {1, 2, 3, 5}
# y = {'e', 'ert'}
# z = {33, 55, 3, 2, 1}
# print(x | y | z)
# # &-амперсант
# print(x & z)  # пересечение множеств. т.е. одинаковые элементы в 2х множествах
#
# print(z - x)
# print(x - z)
#
# t = z.copy()
# print(t)
#
# p = x.isdisjoint(z) # проверка множества является ли пересечением. если множества не содержат общие элементы то True. Содержит false
# print(p)

# a = frozenset([1, 4, 'rete', 34, ])  # создание замороженного множества

# a = {1, 'q', 33, 'ds', 9, 9, 5, 4}
# a.add('33333333')  # добавление во множество
# print(a)

# import random
# c = [random.randint(0, 9) for i in range(6)]
# print(c)
# a = set(c)
# print(a)
# if len(c) == len(a):
#     print('дубликатов нет')
# else:
#     print('в списке есть дубликаты')


# import random
#
# c = set([random.randint(0, 9) for i in range(10)])
# a = frozenset([random.randint(0, 9) for i in range(10)])
#
# print(a)
# print(c)
#
# a1 = {3, 6, 8, 9}
# print(a1)
# b1 = frozenset([1, 2, 3, -10, 40])
# print(b1)
# print(a1 | b1)
# print(a1 & b1)


st = []
num = []

a = {1, 42, 'a', 'asd', 5, 6, 7, 2, 2, 2}
for i in a:
    if type(i) is int:
        num.append(i)
    elif type(i) is str:
        st.append(i)
num.sort()
st.sort(key=len)
print(num, st)