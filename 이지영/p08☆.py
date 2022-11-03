'''
주어진 평가점수 리스트에서 최소값과 최대값을 하나씩 제외한 값들의 평균을 구하라
max(),min(),sum(),len()함수 사용
'''

score = [80,90,100,60,70,85,60]
maxnm = int(max(score))
minnm = int(min(score))

for i in score:
#최소값 제외
    score = [0]
    if score<minnm:
        del minnm

    #최대값 제외

    if score>maxnm:
        del maxnm

#갯수
len(score)

#평균
avr = sum(score)/len(score)
avvv = "{:g}".format(avr)

print("최소값:",min(score),"최대값:",max(score),"갯수:",len(score),"평균:",avvv)