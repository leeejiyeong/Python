'''
리스트에 요소 추가 : insert, append함수
'''
#키보드로부터 숫자 5개를 입력받아서 리스트에 저장
arr = []

#반복 5번(for문) - 자바스크립트라면 for(i=1; i<5;i++)였을거임
for i in range(5):
    #키보드입력
    a = input()
    #리스트에 추가
    arr.append(a)
    
#리스트출력
print(arr)

