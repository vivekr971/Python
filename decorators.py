def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator # Applying the decorator to a function; shorthand for greet = decorator(greet).
def greet():
    print("Hello, World!")
greet()

# Explanation:

# decorator takes the greet function as an argument.
# It returns a new function (wrapper) that first prints a message, 
# calls greet() and then prints another message.
# @decorator syntax is a shorthand for greet = decorator(greet).

# -------------------------------------------------------------------------------

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

# Using the static method
res = MathOperations.add(5, 3)
print(res)

# Explanation:

# add is a static method defined with @staticmethod decorator.
# It can be called directly on class MathOperations without creating an instance.

#----------------------------------------------------------------------------------------
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):                                
        cls.school = new_name #Changes class variable for ALL objects

Student.change_school("XYZ School")
print(Student.school)

# cls = class itself (Student)
# NOT object