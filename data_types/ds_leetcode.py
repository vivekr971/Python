'''
####Rotate Array
def rotate(nums, k):
    if k == k % len(nums):
       nums[:] = nums[-k:] + nums[:k+1]
       return(nums)
print(rotate([1,2,3,4,5,6,7], 3))'''

####Palindrome
'''def palin(s):
    s = ''.join(c.lower() for c in s if c.isalnum())

    if s[:] == s [::-1]:
        return True
    return False

print(palin("A man, a plan, a canal: Panama"))'''
'''
def palin(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    x = 0
    y = len(s)-1

    while x<y:
        if s[x] == s[y]:
            x+=1
            y-=1
        else:
            return False
    return True
print(palin("A man, a plan, a canal: Panama"))'''


# Two Sum (Sorted)
'''
def twosum (nums, target):
    x = 0
    y = len(nums)-1
    while x<y:
        if nums[x]+nums[y] < target:
            x+=1
        elif nums[x]+nums[y] > target:
            y-=1
        else:
            return (x+1,y+1)
print(twosum(nums = [2,7,11,15], target = 9))'''

# Two Sum (UnSorted)
'''
def twosum (nums, target):
    d={}
    ans= len(nums)

    for i in range(ans):
        var = target - nums[i] #nums as it is list not ans
        if var not in d:
            d[nums[i]] = i
        else:
            return(d[var],i)
print(twosum(nums = [2,7,11,15], target = 9)) '''



