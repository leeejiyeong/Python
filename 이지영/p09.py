score = [{'no':1, 'kor':100, 'eng':90, 'mat':90},
        {'no':2, 'kor':30, 'eng':20, 'mat':50},
        {'no':3, 'kor':80, 'eng':90, 'mat':30},
        {'no':4, 'kor':70, 'eng':50, 'mat':10},
        ]

#합계
mathsum = 0
for a in score:
    mathsum += a['mat']

#평균
mathavg = mathsum/len(score)

#출력
maav = "{:g}".format(mathavg)
print("수학성적의 합:",mathsum,"평균:",maav)
