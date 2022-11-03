#함수를 만들자
def mymin(*nums):
    #요소 초기화
    idxnum = 0
    #리스트 수만큼 반복
    for i in nums:
        #작으면
        if i <idxnum :
        #저장
            idxnum=i
    #결과리턴
    return idxnum


result = mymin(3,5,10,2,1)
print(result)