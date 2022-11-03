
arr = [1,2,3,4,5]#map(int(),input().split(' '))
# for i in range(len(arr)):
#     arr[i] = int(arr[i])
print(arr)
# for i in range(arr):
#     el = arr[i] * arr[i]

def power(item):
    return item**2
# for i in range(len(arr)):
#     arr[i] = arr[i] **2

arr = list(map(lambda item : item**2 ,arr))

for el in arr:
    print(el)