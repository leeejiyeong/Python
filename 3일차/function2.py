'''
지역변수, 전역변수
'''

from tkinter import N

#함수선언
#1~10까지 합계
def mysum(n):
    total = 0
    for i in range(n+1): #0~10까지 반복됨
        total +=i
    return total #나는 계산만할게 니가 알아서 적으삼

#함수실행(=호출)-> 함수이름 적으면됨
num = int(input("숫자입력"))
t1 = mysum(num)
print("합계는",t1)

num = int(input("숫자입력"))
t1 = mysum(num)
print("합계는",t1,"입니다!")