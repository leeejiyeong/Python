'''
숫자야구게임
'''
#컴퓨터 난수 3개
from random import randint
import sys

while True:
    c1=randint(1,9)
    while True:
        c2=randint(1,9)
        if c2 !=c1:
            break
    while True:
        c3=randint(1,9)
        if c3 != c1 and c3 !=c2: 
            break

    print(c1,c2,c3)

    cnt = 0     #시도횟수
    s=0
    while s !=3 and cnt<5:  #스크라이크가 3회보다 작고 시도횟수가 5회보다 작으면
        cnt +=1
    #게이머가 숫자입력
        n1,n2,n3 = input().split(' ')
        #정수형으로 변환
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        s=0
        b=0
        #스트라이크 수 계산
        #첫번째 자리 비교
        if c1 == n1:
            s +=1
        #두번째,세번째 자리비교
        if c2 == n2:
            s +=1
        if c3 == n3:
            s +=1

        print(s,"스크라이크")
        #스크라이크 3개면 "ㅊㅋ"메시지 출력
        
        
        #볼 개수 계산
        if c1 == n2 or c1 == n3:
            b +=1
        if c2 == n1 or c2 == n3:
            b +=1
        if c3 == n1 or c3 == n2:
            b +=1

        print(b,"볼")
    exitYn = input("게임을 계속 할까요? Y/N")
    if exitYn in['n','N']:
        break


#스트라이크가 3이면 "ㅊㅋ"라고 출력하고
#시도횟수 3회만에 "천재"
#시도횟수 5회 "우수"
#아니면 보통
#스트라이크가 3이 아니면 "게임오바"
  #quit() =>끝내고 나가는 함수
if s ==3:
    print("ㅊㅋ")
    if cnt<=3:
        print("천재")
        sys.exit()
    elif cnt<=5:
        print("우수")
        sys.exit()
    else:
        print("보통")
if s !=3:
    print("-- GAME OVER --")