
score = [10,-10,1005]

#합계
total = 0
for s in score:
    total += s
print(total) 

#최대값
maxscore = score[0]   #최대, 최소값은 배열의 첫번째값 입력하면 된다.
for s in score:
    if s > maxscore:
        maxscore = s
print("최대:",maxscore)

#최소값
minscore = score[0]   #배열의 첫번째값 입력
for s in score:
    if s < minscore:
        minscore = s
print("최소:", minscore)

maxscore = score[0]
minscore = score[0]

#하나로 합치면
for s in score:
     if s > maxscore:
        maxscore = s
     if s < minscore:
        minscore = s
print("최대:",maxscore)
print("최소:", minscore)