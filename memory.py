import gc

# Create a cycle
def fun(i):
    x = {}
    x[i + 1] = x
    return x

# Trigger garbage collection
c = gc.collect()
print(c)

for i in range(5):
    fun(i)

c = gc.collect()
print(c)
'''
gc.collect() triggers garbage collection and stores the count of collected objects (initially 0).
for i in range(10) calls fun(i) 10 times, creating 10 cyclic references.
gc.collect() triggers garbage collection again and prints the count of collected cycles .
'''


a = [1, 2, 3]
b = {"a": 1, "b": 2}
c = "Hello, world!"

del a,b
print(gc.collect())

#--------------------------------------------------------------------------------------------
a = [1, 2, 3]
b = a

print(id(a), id(b))   # Same ID → both point to same list

b.append(4)
print(a)

#-------------------------------------------------------------------------------
x = 10
y = x

if id(x) == id(y):
    print("x and y refer to same object")

x = 10
y = x
x += 1

if id(x) != id(y):
    print("x and y do not refer to the same object")