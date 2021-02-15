

def describe_car(car_name, car_type='быстро'):
    print(car_name + " разгоняется по дороге "+ car_type)

# Следующие вызовы функций будут идентичны:
describe_car('volvo')
describe_car(car_name='volvo')
describe_car(car_name='volvo', car_type='быстро')
describe_car(car_type='быстро',  car_name='volvo')
