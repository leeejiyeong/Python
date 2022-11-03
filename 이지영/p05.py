movie = ['리맴버','블랙아담','인생은아름다워','스파이럴']

#1. '자백'추가
movie.insert(0,'자백')

#2. '블랙아담'삭제
del movie[2]

#3. 리스트 크기 출력
print("리스트 : 총",len(movie),"개")
print()

#4. 리스트 번호붙이기
for i in range(len(movie)):
    i +=1
    print(i,movie[i-1])

