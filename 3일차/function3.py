'''
전역변수
'''

total = 0

def mysum():
    global total
    for i in range(11):
        total +=i

mysum()
print(total)