# i = 0
# while i < 10:
#     i = i + 1  # i+=1
#     print(i)

# i = 0
# while i < 10:
#     i = i + 1  # i+=1
#     if i == 5:
#         break
#         # continue
#     print(i)

# Необходимо вычислить сумму чисел от 1 до 50 и результат вывести на экран.
# i = 1
# r = 0
# while i <= 50:
#     r = r + i
#     i = i + 1
#     print(i, r)
# print(r)

# r_1 = 0
# for i in range(1, 51):
#     r_1 = r_1 + i
# print(r_1)


#
# a = 0
# while a <= 10:
#     print(a ** 2)
#     a = a + 1


# i = 1
# a = 1
# while i <= 125:
#     if i % 2 == 0:
#         a = a * i
#         print(i, a)
#     i = i + 1
# print('результат:', a)

# for i in range(3):
#     print(i)
#     # if i == 1:
#     #     break
# else:
#     print('Готово')

# i = 0
# while i < 3:
#     if i == 2:
#         break
#     print(i)
#     i = i + 1
# else:
#     print('готово')

# i = 15
# while i > 0:
#     print(i)
#     i = i - 1

# i = 0
# m = []
# while i <= 91:
#     print(i)
#     i = i + 7
#     m.append(i)
# print(m)


a = int(input('a: '))
b = int(input('b: '))
while True:
    c = input('+ - / * 0')
    if c == '+':
        print(a+b)
    elif c == '-':
        print(a-b)