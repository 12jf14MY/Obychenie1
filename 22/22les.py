# class Car:
#     # pass
#     # print(dir(Car))
#
#     # Статические поля
#     default_color = 'Зеленый'
#     default_weight = 3000
#
#     # Динамические поля( переменные объекта)
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#     def turn_on(self):
#         print('222222')
#
#     def ride(self):
#         pass
#     def info(self):
#         print(self.color, self.model)
#
# car_obj = Car('red', 'X7')
# car_obj_2 = Car('green', 'X5')
# car_obj.info()
# car_obj_2.info()
# print(dir(Car))

# print(car_obj.default_color)
# print(car_obj_2.default_color)
# print(car_obj.color)
# print(car_obj_2.color)
# print(car_obj.model)
# print(car_obj_2.model)
# print(car_obj.turn_on())

# #-----------------------------------------------------------------
# class Example:
#     a=1
#     b=2
#
#
#     # Динамические поля( переменные объекта)
#     def __init__(self, ww, sss):
#         self.ww = ww
#         self.sss = sss
#
#     def w1(self):
#         c=3
#         print(c)
#
#     def w2(self):
#         return self.a+self.b
#     def w3(self):
#         return self.ww**self.sss
#
#
# obj_1 =yield Example(4,2)
# obj_1
#
# #-------------------------------------------
# class Example:
#     a = 10
#     b = 20
#     def init(self,qwerty,asd):
#         self.qwerty = qwerty
#         self.asd = asd
#     def first(self):
#         d = 55
#         print(d)
#     def second(self):
#         return self.b + self.a
#     def three(self):
#         return self.qwerty ** self.asd
#
# obj_1 = Example(4,2)
# obj_1.first()
# print(obj_1.second())
# print(obj_1.three())
# print(obj_1.a)

# =====================================================


class Car:

    # Динамические поля( переменные объекта)
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def w1(self):
        print('Авто заведен')

    def w2(self):
        print('Авто заглушен')

    def w3(self):
        print(self.year)

    def w4(self):
        print(self.type)

    def w5(self):
        print(self.color)




#===========================================
class Car:
    # Статические поля (переменные класса)
    default_color = 'Grey'

    # Динамические поля (переменные объекта)
    def init(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    # Методы
    def first(self):
        print('Автомобиль заведен')

    def second(self):
        print('Автомобиль заглушен')

    def third(self):
        print(self.year)

    def fourth(self):
        print(self.type)

    def fifth(self):
        print(self.color)


car_obj = Car('Red', 'BMW', 2021)
print(car_obj.default_color)
print(car_obj.color)
print(car_obj.type)
print(car_obj.year)
print(car_obj.first())
print(car_obj.second())
print(car_obj.third())
print(car_obj.fourth())
print(car_obj.fifth())