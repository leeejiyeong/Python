users = [{'userno':100,'username':'김티모','salary':2000},
         {'userno':101,'username':'박아리','salary':4000},
         {'userno':102,'username':'이애쉬','salary':3500}]

#1.추가 2.삭제 3.조회 4.전체조회 5.종료


while True:
    print('1.추가 2.삭제 3.조회 4.전체조회 5.종료')
    no =  int(input("메뉴번호를 입력하씨오:"))
    if no ==1:
        info={}
        info['userno'] = input("userno입력:")
        info['username'] = input("username입력:")
        info['salary'] = input("salary입력:")
        users.append(info)

    elif no ==2:
        userno = int(input("삭제할 userno:"))
        idx = 0
        for i in users:
            if i['userno'] == userno:
                del users[idx]
                break
            idx +=1

    elif no ==3:
        userno = int(input("조회할 userno입력:"))
        for i in users:
            if i['userno'] == userno:
                print(i['username'],i['salary'])

    elif no ==4:
        print("전체조회")
        for i in users:
            print(i['userno'],i['username'],i['salary'])

    elif no ==5 :
        print("종료")
        break
print("the end")