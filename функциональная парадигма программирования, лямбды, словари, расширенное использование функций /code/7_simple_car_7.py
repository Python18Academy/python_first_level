class Car:
    """Базовый класс автомобиля"""
    def __init__(self, marka, speed):
        """ инициализирует атрибуты марки и скорости автомобиля"""
        self.marka = marka
        self.speed = speed
        self.odometr_reading = 0

    def car_ride(self):
        return "машинка " + self.marka+" едет со скоростью "+ str(self.speed)
    def read_odometr(self):
        """Выведет нам пробег автомобиля """
        print("У этого автомобиля пробег " + str(self.odometr_reading) + " на счетчике")
    def update_odometr(self, kilo_age):
        self.odometr_reading = kilo_age
    def increment_odometr(self, kilometrs, hours):
        """ Увеличивает значения одометра с заданным приращением"""
        self.odometr_reading += kilometrs * hours

#теперь мы сможем обновлять значения одометра с помощью вызова метода
bmw = Car('bmw', 90)
bmw.update_odometr(290)
bmw.read_odometr()
bmw.increment_odometr(100, 3)
bmw.read_odometr()
