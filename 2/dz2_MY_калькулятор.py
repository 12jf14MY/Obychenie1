# Написать примитивный калькулятор. Пользователь должен ввести число,
# потом операцию (+-/*) и потом ещё одно число, после этого пользователь получает ответ.
# Числа могут быть дробными.

print("калькулятор")  # название

a = float(input('введите число a '))  # Запрос пользователя ввести первое любое число
s = input("Введите оператора действия над числами +,-,/,*,%,//,**: ")
b = float(input('введите число b '))  # Запрос пользователя ввести второе целое число
if s == '+':
    print('результат суммы чисел a+b=', a + b)  # вывод на экран операция сложение
elif s == '/':
    print('результат деления чисел a/b=', a / b)  # вывод на экран операция деление
elif s == '*':
    print('результат умножения чисел a/b=', a * b)  # вывод на экран операция умножение
elif s == '%':
    print('результат деления по модулю a%b=', a % b)  # вывод на экран операция деление по модулю
elif s == '//':
    print('результат цельночисленного деления a//b=', a // b)  # вывод на экран целочисленное деление
elif s == '**':
    print('результат возведения в степень a**b=', a ** b)  # вывод на экран операция возведение в степень
else:
    print('результат разницы чисел a-b=', a - b)  # вывод на экран операция вычитание

print('расчет окончен')
