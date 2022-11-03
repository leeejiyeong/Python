'''
리스트 삭제, 조회
'''
members=[
    {'name':'김일번','age':20,'addr':'대구'},
    {'name':'아이번','age':25,'addr':'스울'},
    {'name':'최삼번','age':22,'addr':'붓싼'}
]

#전체출력(이름, 지역)
name = input("검색할 이름 입력:")
for i in range(len(members)):
    if name in members[i]["name"]:     
        print(f'{members[i]["age"]} \t {members[i]["addr"]}')
        del members[i]
        break

print(members)