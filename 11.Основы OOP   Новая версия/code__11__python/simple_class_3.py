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
        print("У этого автомобиля пробег " + str(self.odometr_reading) + "на счетчике")
    def update_odometr(self, mileage):
        self.odometr_reading = mileage



