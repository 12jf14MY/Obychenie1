# class Сar:
#     # создание методов класса
#
#     def __str__(self):
#         return 'carrrrrrr'
#     def star(self):
#         print('Двиг заведен')
#
#
# car_a = Сar()
# print(car_a)

# ============================================================================================
# class Phone:
#     def __unit__(self, color, model):
#         self.color = color
#         self.model = model
#
#         # Обычный метод
#         # первый параметр метода self
#
#     def check_sim(self, mobile_operator):
#         if self.model == '1785' and mobile_operator == ' MTS':
#             print('you mobile operator is MTS')
#
#     @staticmetod
#     def model_hash(model):
#         if model == '1785':
#             return 2525252525
#         elif model == 'K498':
#             return 111111111
#         else:
#             return None
#
#     @classmetod
#     def toy_phone(cls, color):
#         toy_phone = cls(color, 'Toy')
#         return toy_phone
#
#
# Phone.toy_phone('Red')
# print(Phone.toy_phone('Red').model)
#
#
# Print(Phone.model_hash('1785'))
#
# my_phone = Phone('red', '1785')
# print(my_phone.model_hash('K498'))
# my_phone.check_sim('MTS')

# =======================================================================================================================
# Класс Human
# Создайте класс Human.
# Определите для него два статических поля: default_name и default_age.
# Создайте метод init(), который помимо self принимает еще два параметра: name и age.
# Для этих параметров задайте значения по умолчанию, используя свойства default_name и default_age.
# В методе init() определите четыре свойства: Публичные - name и age. Приватные - money и house.
# Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
# Реализуйте справочный статический метод default_info(), который будет выводить статические
# поля default_name и default_age.
# Реализуйте метод earn_money(), увеличивающий значение свойства money

# Класс House
# 1. Создайте класс House
# 2. Создайте метод init() и определите внутри него два динамических свойства: _area и _price.
# 3. Свои начальные значения они получают из параметров метода init()
# 4. Создайте метод final_price(), который принимает в качестве параметра размер скидки и
# возвращает цену с учетом данной скидки.

# Класс SmallHouse
# 1. Создайте класс SmallHouse, унаследовав его функционал от класса House
# 2. Внутри класса SmallHouse переопределите метод init() так, чтобы он создавал объект с площадью 40м2

# Класс Human
#  1. Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию
# покупки дома: уменьшать количество денег на счету и присваивать ссылку на только что купленный дом.
# В качестве аргументов данный метод принимает объект дома и его цену.
# 2.  Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег для
# покупки, и совершать сделку. Если денег слишком мало - нужно вывести предупреждение в консоль.
# Параметры метода: ссылка на дом и размер скидки


class Human:
    default_name = 'A'
    default_age = 6

    def init(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__house = None
        self.__money = 0

    def info(self):
        print(self.name, self.__money, self.__house, self.age)

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def earn_money(self, plus):
        self.__money += plus
        print(self.__money)


human1 = Human('mark', 26)
human1.info()
human1.earn_money(100)
human1.info()


# ==============================================
# class Phone:
#     # Инициализатор
#     def __init__(self):
#         self.is_on = False
#
#     def turn_on(self):
#         pass
#
#     def call(self):
#         pass
#
#
# class MobilePhone(Phone):
#     def __init__(self):
#         super().__init__()
#         self.battery = 0
#
#     def change(self, num):
#         pass
#
#
# my_mobile_phone = MobilePhone()
# print(dir(my_mobile_phone))

# =============================================================
# class Vehicle:
#     def vehicle_metod(self):
#         print('Это родитель класса Vehicle из метода vehicle_metod')
#
#
# class Car(Vehicle):
#     def car_metod(self):
#         print('Это дочерний метод из класса Car')
#
#
# class Cycle(Vehicle):
#     def cycle_metod(sel):
#         print('Это дочерний метод из класса Cycle')
#
#
# ccc = Car()
# ccc.vehicle_metod()
# fff = Cycle()
# fff.vehicle_metod()
#
#
# #=================================================

# class Camera:
#     def camera_method(self):
#         print("Это родительский метод из класса Camera")
# class Radio:
#     def radio_method(self):
#         print("Это родительский метод из класса Radio")
# class CellPhone(Camera, Radio):
#     def cell_phone_method(self):
#         print("Это дочерний метод из класса CellPhone")
# cell_phone_a = CellPhone()
# cell_phone_a.camera_method()
# cell_phone_a.radio_method()

#===========================================================


