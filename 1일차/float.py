'''
실수값 2개를 입력받아서 합계를 계산하고 출력하는 프로그램 작성
'''


#입력
x = input()
a,b = x.split(" ") #문자 자르기

#실수형으로 변환
a = float(a)
b = float(b)

#합계 계산
total = a + b

#결과 출력
print(total)