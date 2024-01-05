# Variables
integer_variable = 42
float_variable = 3.14
boolean_variable = True
string_variable = "Python is fun!"

# Lists 
int_list = [1, 2, 3, 4, 5]
string_list = ["apple", "banana", "orange"]

# Dictionary 
age_dict = {"Alice": 25, "Bob": 30}

# Set 
unique_set = {"Apple", "Orange", "Apple"}  # Duplicate element is ignored

# For loop
print("Printing elements of int_list:")
for num in int_list:
    print(num, end=" ")  


# While loop
counter = 1
print("Example of a while loop:")
while counter <= 5:
    print("Iteration", counter)
    counter += 1

# Function
def display_message(message):
    print(message)

# Function calling
display_message("Hello from a function!")

# Class and object
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name + " says Woof!")

# Object creation and method call
my_dog = Dog("Buddy", 3)
my_dog.bark()

# User input
user_input = input("Enter something: ")
print("You entered:", user_input)
