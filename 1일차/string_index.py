'''
문자열 인덱싱(자르기)
'''

#인덱싱
a = "920315"

#한글자만 추출하기
print("첫번째문자",a[0])
print("마지막문자",a[-1])
print("출생년도",a[:2])
print("출생월",a[ : ])
print("출생일", a[-2:])
print("에러", a[7])
