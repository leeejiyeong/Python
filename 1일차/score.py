"""
점수 3개를 입력받아서 합계를 구하는 프로그램
말로 코드를 짜보는거 = 수도코드
"""
#입력
s = input()    #90 30 50

#문자 자르기
score = s.split(" ")

#정수형으로 변환
kor = int(score[0])
eng = int(score[1])
mat = int(score[2])

#합계
total = kor + eng + mat

#평균
aver = total/3

#출력 : 평균이 90이상->수, 80이상->우,70이상->미, 나머지->양
print(total) 

if aver>=90:
    print("수")
elif aver>=80:
    print("우")
elif aver>=70:
    print("미")
else:
    print("양")
