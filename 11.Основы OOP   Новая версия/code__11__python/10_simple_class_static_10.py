class Car:
    """Базовый класс автомобиля"""
    def __init__(self, marka, speed):
        """ инициализирует атрибуты марки и скорости автомобиля"""
        self.marka = marka
        self.speed = speed
        self.odometr_reading = 0

    @staticmethod
    def get_class_details():
        print("Это класс")
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


#статичный метод можно вызвать напрямую из класса
# Car.get_class_details()
class ElectricCar(Car):
    """ Представляет класс автомобиля с элетродвигателем"""

    def __init__(self, marka, speed):
        """ Инициализирует атрибуты класса -родителя
            затем можно добавить атрибуты, которые специфичны именно для этого класса
        """
        super().__init__(marka, speed)
        # self.battery = Battery()
print(ElectricCar.get_class_details())