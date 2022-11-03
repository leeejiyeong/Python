'''
kor 성적이 60미만인 학생의 no를 출력하는 코드작성
filter, lambda사용
'''

score = [{'no':1, 'kor':100, 'eng':90, 'mat':90},
        {'no':2, 'kor':30, 'eng':20, 'mat':50},
        {'no':3, 'kor':80, 'eng':90, 'mat':30},
        {'no':4, 'kor':70, 'eng':50, 'mat':10},
        ]

arr = list(filter(lambda item : item['kor']<60, score))

print(arr['no'])

