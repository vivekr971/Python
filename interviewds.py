'''
posts = [ {"id": 1, "status": "safe"}, 
{"id": 2, "status": "spam"}, 
{"id": 3, "status": "safe"},
 {"id": 4, "status": "spam"}, 
 {"id": 5, "status": "ban"},
 here we need to arrange it in such a way that the output has all the things 
 like ["safe":2,1,3] like how many times everything has come along with it id



def var(posts):

    count={}

    for i in posts:
        x = i["status"]
        y = i["id"]

        if x not in count:
            count[x]=[]

        count[x].append(y)
    return count

def var(posts):
    count = {}

    for post in posts:
        status = post["status"]
        id = post["id"]

        if status not in count:
            count[status] = [0]      # First element stores the count

        count[status][0] += 1        # Increment count
        count[status].append(id)     # Append ID

    return count
posts = [ {"id": 1, "status": "safe"}, 
{"id": 2, "status": "spam"}, 
{"id": 3, "status": "safe"},
 {"id": 4, "status": "spam"}, 
 {"id": 5, "status": "ban"},]

print(var(posts))

--------------------------------------------------
Q2
'''
def var(strs, orderInd):

    
    vowels = "aeiouAEIOU"
    result = []

    for i in orderInd:
        count = 0

        for ch in strs[i]:
            if ch in vowels:
                count += 1

        result.append((strs[i], count))

    return result


print(var(
    ["hello", "waltham", "I", "am", "here"],
    [3, 4, 1, 0, 2]
))








strs = ["hello","waltham","I", "am", "here"]
orderInd = [3,4,1,0,2]


print(var(strs, orderInd ))