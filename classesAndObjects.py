# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

#Define Cars
car1 = Vehicle()
car2 = Vehicle()

#Set the values of the variables in the vehicle class for car1
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.00

#Set the values of the variables in the vehicle class for car2
car2.name = "Jump"
car2.kind = "Van"
car2.color = "blue"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())

