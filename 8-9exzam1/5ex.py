# 5. Вводится строка, содержащая буквы, целые неотрицательные числа и иные символы.
# Требуется все числа, которые встречаются в строке отдельно вывести на экран.
# Строка может содержать пробелы.

a = input('Введите любую строку с пробелами, буквами и цифрами: ')
b = ''
for i in a:
    #print(i)
    if i.isdigit():  #если i число, то.....
        #print(b)
        b = b + i    #..... то записываем в пустую строку
print('Результат вывода чисел', b)
print('конец')