class Car:
    """Базовый класс автомобиля"""
    def __init__(self, marka, speed):
        """ инициализирует атрибуты марки и скорости автомобиля"""
        self.marka = marka
        self.speed = speed
    def car_ride(self):
        return "машинка " + self.marka+" едет со скоростью "+ str(self.speed)


bmw = Car("bmw", 90)

# print(bmw.car_ride())
# del bmw.speed
# print(bmw.speed)
for attr in dir(bmw):
    if attr[0] == '_':
        print(attr)
for item in bmw.__dict__:
    print(item, bmw.__dict__[item])