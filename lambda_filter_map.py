
add = lambda a, b: a + b

print(add(2, 3))


# a, b → inputs
# a + b → returned automatically
# 🚨 No need to write return

check = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check(5))   
print(check(-3))  
print(check(0))


check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(4))  
print(check(7))

calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)

# Although a lambda can contain only one expression, 
# it can still return multiple results by combining them into a tuple.


#---------------------------------------------------
number=[1,2,3,4,5,6,7,8,9]

# def is_even(num):
#     return num % 2 == 0

# result = filter(is_even, number)
# print(list(result))

#---------------------------------------------

result = filter(lambda x: x % 2 == 0, number)

print(list(result))

names = ["Vivek", "", "Rahul", "", "Amit"]

result = filter(lambda name: name != "", names)

print(list(result))

#-----------------------------------------------
numbers = [1, 2, 3, 4]

def square(x):
    return x * x

result = map(square, numbers)

print(list(result))

#---------------------------------------------
names = ["vivek", "rahul", "amit"]

result = map(lambda name: name.upper(), names)

print(list(result))

#-----------------------------------------------
numbers = [1, 2, 3, 4, 5]

# map → change values
print(list(map(lambda x: x * 10, numbers)))

# filter → select values
print(list(filter(lambda x: x % 2 == 0, numbers)))

#---------------------------------------------------

from functools import reduce

nums = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, nums)

print(result)

# This is how reduce works internally:

# Step 1: a=1, b=2 → 3  
# Step 2: a=3, b=3 → 6  
# Step 3: a=6, b=4 → 10 

from functools import reduce
a = [5, 9, 3, 12, 7]
r = reduce(lambda x, y: x if x > y else y, a)
print(r)

##With Initial Value (Important)
from functools import reduce
nums = [1, 2, 3]

result = reduce(lambda a, b: a + b, nums, 5)
print(result)


#-----------------------------------------------------




