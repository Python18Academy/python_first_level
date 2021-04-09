def intro(**data):
    print("\nData type of argument: ",type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))

intro(Firstname="Petr", Lastname="Ivanov", Age=22, Phone=1234567890)
intro(Firstname="Semen", Lastname="Semenov", Email="semen@example.com", Country="Pussia", Age=25, Phone=9876543210)