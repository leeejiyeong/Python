
users = [{'userno':100,'username':'user1','salary':2000},
         {'userno':101,'username':'user2','salary':1000},
         {'userno':102,'username':'user3','salary':1500}]

while True:
    print("1.추가 2.삭제 3.조회 4.전체조회 5.종료")
    no = int(input("메뉴선택:"))
    if no ==1:
            info={ }
            info["userno"] = int(input("번호입력:"))
            info["username"] = input("이름입력:")
            info["salary"] = int(input("급여입력:"))
            users.append(info)

    elif no ==2:
        userno = int(input("삭제할 번호:"))
        idx = 0
        for i in users:
             if i["userno"] == userno:
                del users[idx]
                break
             idx +=1

    elif no ==3:
        #번호를 입력
        userno = int(input("조회할 번호:"))
        #해당번호의 이름과 급여 출력
        for i in users:
            if i["userno"] == userno:
                print(i['username'],i['salary'])

    elif no ==4:
        print("전체조회")
        #이름, 급여 출력
        for a in users:
            print(a['username'],a['salary'])

    elif no ==5 :
        print("종료")
        break
print("The End")