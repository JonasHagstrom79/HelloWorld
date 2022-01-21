#Objects are an encapsulation of variables and functions into a single entity.
# Objects get their variables and functions from classes. Classes are essentially
# a template to create your objects.

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class")

#To assign the class to an object
myobjectx = MyClass()

#To access the variable inside
print(myobjectx.variable)

#To access the function

myobjectx.function()

#Class defined for vehicles

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_string = "%s is a %s %s worth $%.2f" % (self.name, self.color, self.kind,
                                                     self.value)
        return desc_string

car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

print(car1.description())
print(car2.description())