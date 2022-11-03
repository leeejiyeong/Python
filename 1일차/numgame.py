
from random import randint
import sys

c = randint(1,100)

# print(c)

cnt = 0
n = input()
n = int(n)

while c !=n and cnt<10:
    cnt +=1

    if n == c:
        print("정답입니다")
        sys.exit()
    elif n > c:
        print("더 큰수입니다")
    else:
        print("더 작은수입니다")

if n==10:
    print("game over")