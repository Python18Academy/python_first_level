class Car:
    """Базовый класс автомобиля"""

    def __init__(self, marka, speed):
        """ инициализирует атрибуты марки и скорости автомобиля"""
        self.marka = marka
        self.speed = speed
        self.odometr_reading = 0

    def car_ride(self):
        return "машинка " + self.marka + " едет со скоростью " + str(self.speed)

    def read_odometr(self):
        """Выведет нам пробег автомобиля """
        print("У этого автомобиля пробег " + str(
            self.odometr_reading) + " на счетчике")

    def update_odometr(self, kilo_age):
        self.odometr_reading = kilo_age

    def increment_odometr(self, kilometrs, hours):
        """ Увеличивает значения одометра с заданным приращением"""
        self.odometr_reading += kilometrs * hours


class Battery():
    """ Простой класс аккумулятора, который может обслуживать нащ автомобиль"""

    def __init__(self, battery_size=120):
        """инициализируем атрибуты аккумулятора
            по умолчанию наш аккумулятор будет заряжен на 120
        """
        self.battery_size = battery_size
    def show_akk(self):
        print("В аккумуляторе автомобиля осталось только " + str(self.battery_size))



class ElectricCar(Car):
    """ Представляет класс автомобиля с элетродвигателем"""

    def __init__(self, marka, speed):
        """ Инициализирует атрибуты класса -родителя
            затем можно добавить атрибуты, которые специфичны именно для этого класса
        """
        super().__init__(marka, speed)
        self.battery = Battery()




myTesla = ElectricCar('tesla', 300)
myTesla.battery.show_akk()
print(myTesla.car_ride())
# myTesla.read_o    dometr()