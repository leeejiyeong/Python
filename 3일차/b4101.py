'''
두 양의 정수가 주어졌을 때, 첫 번째 수가 두 번째 수보다 큰지 구하는 프로그램을 
작성하시오.

입력은 여러 개의 테스트 케이스로 이루어져 있다. 
각 테스트 케이스는 한 줄로 이루어져 있으며, 두 정수가 주어진다. 
두 수는 백만보다 작거나 같은 양의 정수이다. 입력의 마지막 줄에는 0이 두 개 
주어진다.

각 테스트 케이스마다, 첫 번째 수가 두 번째 수보다 크면 Yes를, 
아니면 No를 한 줄에 하나씩 출력한다.
'''
'''
매개변수 : 숫자 2개
리턴값 : yes, no, 0
'''
def test():
    result = 0
    if a ==b==0:
        result =0
                #크면 yes 출력
    if a>b:
        result("yes")
                #아니면 no 출력
    else:
        result("no")

#반복문(while)
while True:
    #숫자 두개 입력
    a,b = input().split(" ")
    a=int(a)
    b=int(b)
        #===========함수호출==========
            #숫자 2개가 0이면 종료
    result= test(a,b)
    if result ==0:
        break
    else:
        print(result)
 
        #결과출력
