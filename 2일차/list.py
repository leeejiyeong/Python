'''
리스트 다루기
'''

list =[]
for i in range(3):
    info = {}

    #이름입력
    info["name"] = input("이름입력:")
    #나이입력
    info["age"] = input("나이입력:")
    #주소입력
    info["addr"] = input("주소입력:")

    #리스트에 추가
    list.append(info)

#list 출력(for문 사용하여 이름,나이)
for info in list: 
    print(f'{info["name"]}\t{info["age"]}')