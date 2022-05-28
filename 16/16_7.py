# Напишите программу, демонстрирующую работу try\except\finall

try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    c = int(a)/int(b)
except (ValueError, ZeroDivisionError):
    print("Ошибка ввода или деления на 0...")
else:
    print("Результат в квадрате: ", c**2)
finally:
    print(" Здесь был finally и он все видел ")