
#학생의 성적을 계산하는 프로그램
std = [ {"mat":50, "eng":80},
        {"mat":40, "eng":70},
        {"mat":30, "eng":90}]

#수학성적의 합계
matSum = 0
for score in std:
    matSum += score['mat']
print(matSum)

'''
in뒤에는 배열이름
score는 중괄호로 묶였으니까 이름 적어줘야됨 =>['math']
'''