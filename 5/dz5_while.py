# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

a = float(input('введите число a '))  # Запрос пользователя ввести первое любое число
b = float(input('введите число b '))  # Запрос пользователя ввести второе целое число
while True:
    s = input("Введите действие над числами +,-,/,*,%,//,**, 0 - выход: ")
    if b == 0 and s == '/' or s == '//':
        print('На 0 делить нельзя. Повторите ввод')
        continue
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
    elif s == '-':
        print('результат разницы чисел a-b=', a - b)  # вывод на экран операция вычитание
    elif s == '0':
        print('0-звершение работы')  # вывод на экран операция возведение в степень
        break
    else:
        print('не верное значение повторите ввод')