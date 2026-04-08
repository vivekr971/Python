# a = [1, 2, 3]
# b = ['a', 'b', 'c']

# # No iterable are passed
# res = zip()
# print(list(res))

# # One iterable is passed
# res = zip(a)
# print(list(res))

# # Two iterables are passed
# res = zip(a, b)
# print(res)

def isPalindrome(s: str) -> bool:
    s = s.replace(" ", "").lower()
    s = s.replace(",", "")
    s = s.replace(":", "")
    j = len(s)-1
    for i in range (len(s)):
        if  s[i] == s[j]:
            j= j-1
        else:
            return False
    return True
print(isPalindrome (s = "a man, a plan, a canal: Panama"))

def twoSum(numbers: list[int], target: int):
    x = 0
    y = len (numbers) - 1
    while x<y:
        if numbers[x] + numbers[y] < target:
            x+=1
        elif numbers[x] + numbers[y] > target:
            y-=1
        else:
            numbers[x] + numbers[y] == target
            
            return (x,y)
print(twoSum(numbers = [2,7,11,15], target = 9))
'''
If sum == target → return
If sum < target → move left pointer (x++)
If sum > target → move right pointer (y--)
'''