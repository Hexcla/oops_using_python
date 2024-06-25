class Vehicle:
    def vehicle_info(self):
        print("It is parent class")

class car(Vehicle):
    def car_info(self):
        print("It is subclass_1")

class sport_car(Vehicle):
    def sport_car_info(self):
        print("It is subclass_2")

class car_version(Vehicle):
    def car_version_info(self):
        print("It is subclass_3")

sub_class_1 = car()
sub_class_2 = sport_car()
sub_class_3 = car_version()

print(sub_class_1.vehicle_info())
print(sub_class_2.vehicle_info())
print(sub_class_3.vehicle_info())

    
