arr=[3,8,4,2,6,9,5]

newarr=[]
'''
for el in arr:
    if el>5:
        newarr.append(el)
'''
def comp(item):
    return item >5

newarr = list(filter(lambda el : el>5, arr))
print(newarr)
