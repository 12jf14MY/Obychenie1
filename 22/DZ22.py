# Калькулятор.
# Создайте класс, где реализованы функции(методы) математических операций.
# А также функция, для ввод данных.

class calculator:

    def vvod(self,a,b,s):
        self.a = float(input('введите число a '))  # Запрос пользователя ввести первое любое число
        self.b = float(input('введите число b '))  # Запрос пользователя ввести второе целое число
        self.s = input("Введите действие над числами +,-,/,*,%,//,**, 0 - выход: ")


    def fun1(self,a, b):
        return a+b  #  операция сложение

    def fun2(self,a, b):
        return a/b  #  операция деление

    def fun3(self,a, b):
        return a*b #  операция умножение

    def fun4(self,a, b):
        return a%b #  операция деление по модулю

    def fun5(self,a, b):
        return a//b #  целочисленное деление

    def fun6(self,a, b):
        return a**b  #  операция возведение в степень

    def fun7(self,a, b):
        return a-b #  операция вычитание

    def fun8(self,a, b):
        print('0-звершение работы')  # вывод на экран операция возведение в степень

    def fun9(self,a, b):
        print('На 0 делить нельзя. Повторите ввод')



    def vv(self,s):
        if s == '+':
            fun1(a, b)
        elif s == '/':
            fun2(a, b)
        elif s == '*':
            fun3(a, b)
        elif s == '%':
            fun4(a, b)
        elif s == '//':
            fun5(a, b)
        elif s == '**':
            fun6(a, b)
        elif s == '-':
            fun7(a, b)
        elif s == '0':
            fun8(a, b)
            # break
        else:
            print('не верное значение повторите ввод')
while True:
    # if b == 0 and s == '/' or s == '//':
    #         fun9(a, b)
    #         continue
    obj1=vvod()
