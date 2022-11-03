"""
점수 3개를 입력받아서 합계를 구하는 프로그램
말로 코드를 짜보는거 = 수도코드
"""
#입력
# s = input()    #90 30 50 

# #문자 자르기
# kor,eng,mat = s.split(" ")
kor,eng,mat = input().strip().split(' ')

#정수형으로 변환
kor = int(kor)
eng = int(eng)
mat = int(mat)

#합계
total = kor + eng + mat

#출력
print(total)
#국어:  영어:  수학:
#합계는 00입니다.
print("국어:{:5d} 영어:{} 수학:{} \n합계는{}입니다.".format(kor,eng,mat,total))
print(f"국어:{kor} 영어:{eng} 수학:{mat} \n합계는{total}입니다.")
