'''
제일 큰 수 찾는 함수
매개변수 : 정수형값들
리턴값 : 정수형
'''

def mymax(*nums):
    #결과(제일큰 수)를 저장할 변수를 첫번째 요소로 초기화
    idxnum = 0
    #리스트 수만큼 반복
    for i in nums:
        #리스트 요소의 값이 크다면
        if i>idxnum:
        #변수에 저장
            idxnum=i
        
    #결과를 리턴
    return idxnum


result = mymax(3,5,10,2)
print(result)