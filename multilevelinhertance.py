class Vehicle:
    def vehicle_info(self):
        print("It is parent class")
class car(Vehicle):
    def car_info(self):
        print("It is subclass_1")
class sport_car(car):
    def sport_car_info(self):
        print("It is subclass_2")

sub_3 = sport_car()
print(sub_3.car_info())
print(sub_3.vehicle_info())
print(sub_3.sport_car_info())

    
