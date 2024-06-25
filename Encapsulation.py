class Student:
    def __init__(self, name, age):
        self.__name = name

    # Getter method
    def get_name(self):
        return self.__name

    # Setter method
    def set_name(self, new_name):
        self.__name = new_name

student = Student("Bob", 22)
print("Original name:", student.get_name())

# Modify the name using the setter
student.set_name("Charlie")
print("Modified name:", student.get_name())
