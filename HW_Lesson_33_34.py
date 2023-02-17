'''Задание 1
Создайте класс Circle (окружность). Для данного
класса реализуйте ряд перегруженных операторов:
■ Проверка на равенство радиусов двух окружностей
(операция = =);
■ Сравнения длин двух окружностей (операции >, <,
<=,>=);
■ Пропорциональное изменение размеров окружности,
путем изменения ее радиуса (операции + - += -=).'''

class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.c = 2 * 3.14 * self.radius

    def __str__(self):
        return f'Radius = {self.radius}\nCircle = {self.c}'

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.c < other.c

    def __le__(self, other):
        return self.c <= other.c

    def __gt__(self, other):
        return self.c > other.c

    def __ge__(self, other):
        return self.c >= other.c

    def __add__(self, other):
        r = self.radius + other.radius
        cir = 2 * 3.14 * r
        return f'Radius = {r}\nCircle = {cir}'

    def __sub__(self, other):
        if other.radius <= self.radius:
            r = self.radius - other.radius
            cir = 2 * 3.14 * r
            return f'Radius = {r}\nCircle = {cir}'
        elif other.radius >= self.radius:
            r = other.radius - self.radius
            cir = 2 * 3.14 * r
            return f'Radius = {r}\nCircle = {cir}'

    def __iadd__(self, other):
        self.radius += other.radius
        self.c = 2 * 3.14 * self.radius
        return self

    def __isub__(self, other):
        if other.radius <= self.radius:
            self.radius -= other.radius
            self.c = 2 * 3.14 * self.radius
            return self
        elif other.radius >= self.radius:
            other.radius -= self.radius
            other.c = 2 * 3.14 * other.radius
            return f'Radius = {other.radius}\nCircle = {other.c}'


a = Circle(4)
b = Circle(10)
print(a)
print(b)
print(a == b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
print(a - b)
print(a + b)
a += b
print(a)
a -= b
print(a)

'''Задание 2
Создайте класс Complex (комплексное число). Более
подробно ознакомиться с комплексными числами можно
по ссылке.
Создайте перегруженные операторы для реализации
арифметических операций для по работе с комплексными
числами (операции +, -, *, /).'''

class Complex:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.complex_number = complex(self.a, self.b)

    def __str__(self):
        return f'Complex number = {self.complex_number}'

    def __add__(self, other):
        return self.complex_number + other.complex_number

    def __sub__(self, other):
        return self.complex_number - other.complex_number

    def __mul__(self, other):
        return self.complex_number * other.complex_number

    def __truediv__(self, other):
        return self.complex_number / other.complex_number


a = Complex(3, 4)
b = Complex(2, 6)
print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)

'''Задание 3
Вам необходимо создать класс Airplane (самолет).
С помощью перегрузки операторов реализовать:
■ Проверка на равенство типов самолетов (операция
= =);
■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
■ Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции >
< <= >=).'''

class Airplane:
    def __init__(self, type_airplane, passenger, max_passenger):
        self.type_airplane = type_airplane
        self.passenger = passenger
        self.max_passenger = max_passenger

    def __str__(self):
        return f'Type : {self.type_airplane},\nAmounts of passengers : {self.passenger},\nMaximum possible number of passengers : {self.max_passenger}'

    def __eq__(self, other):
        if self.type_airplane == other.type_airplane:
            return self
        else:
            return f"{self.type_airplane} and {other.type_airplane} are not the same "

    def __add__(self, other):
        new_amount = self.passenger + other.passenger
        if 0 < new_amount <= self.max_passenger:
            return f'New amounts of passengers = {new_amount}'
        else:
            return f'Number of passengers cannot be more {self.max_passenger}'

    def __sub__(self, other):
        if other.passenger >= self.passenger:
            return f'Number of passengers cannot be less than 0'
        else:
            return f'New amounts of passengers = {self.passenger}'

    def __iadd__(self, other):
        self.passenger += other.passenger
        if self.passenger < self.max_passenger:
            return f'New amounts of passengers = {self.passenger}'
        else:
            return f'Number of passengers cannot be more {self.max_passenger}'

    def __isub__(self, other):
        self.passenger -= other.passenger
        if self.passenger < 0:
            return f'Number of passengers cannot be less than 0'
        else:
            return f'New amounts of passengers = {self.passenger}'

    def __lt__(self, other):
        return self.max_passenger < other.max_passenger

    def __le__(self, other):
        return self.max_passenger <= other.max_passenger

    def __gt__(self, other):
        return self.max_passenger > other.max_passenger

    def __ge__(self, other):
        return self.max_passenger >= other.max_passenger


boeing = Airplane('Passenger', 350, 940)
mriya = Airplane('Trucking', 6, 70)
print(boeing)
print(mriya)
print(boeing == mriya)
print(boeing + mriya)
print(boeing - mriya)
# mriya += boeing
# print(mriya)
# boeing -= mriya
# print(boeing)
# mriya -= boeing
# print(mriya)
print(boeing < mriya)
print(mriya < boeing)
print(boeing > mriya)
print(mriya > boeing)
print(boeing <= mriya)
print(mriya <= boeing)
print(boeing >= mriya)
print(mriya >= boeing)

'''Задание 4
Создать класс Flat (квартира). Реализовать перегруженные операторы:
■ Проверка на равенство площадей квартир (операция
==);
■ Проверка на неравенство площадей квартир (операция !=);
■ Сравнение двух квартир по цене (операции > < <= >=).'''


class Flat:

    def __init__(self, area, price, floor, district, city):
        self.area = area
        self.price = price
        self.floor = floor
        self.district = district
        self.city = city

    def __str__(self):
        return f'Area = {self.area},\nFloor = {self.floor},\nDistrict = {self.district},\nCity = {self.city},\nPrice = {self.price}'

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price


my_flat = Flat(60, 55000, 2, 'Deribasivska', 'Odesa')
new_flat = Flat(100, 140000, 18, 'Milanska', 'Odesa')
print(my_flat)
print()
print(new_flat)
print(my_flat == new_flat)
print(my_flat != new_flat)
print(my_flat < new_flat)
print(my_flat <= new_flat)
print(my_flat > new_flat)
print(my_flat >= new_flat)
