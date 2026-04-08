def fun(max):
    cnt=5

    while cnt < max:
        yield cnt
        cnt+=1
    
for i in fun(10):
    print (i)

'''
This generator function fun yields numbers from 5 up to a specified max. Each call to next() 
on the generator object resumes execution right after the yield statement, where it last left off.

'''
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up_to(3)

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

def fun():
    yield 100          
    yield "vivek"          
    yield True         
 
# Driver code to check above generator function
for val in fun(): 
    print(val)


gen = (x * x for x in range(5))

for i in gen:
    print(i)


#------------------------------------------------------------------------------------------

num=["gdsl",2,5]

var = iter(num)

print (next(var))

#-----------------------------------------------------------------------------------