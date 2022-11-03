'''
3일차 user_manage.py
'''

'''======================
메뉴선택
리턴값 : 입력된 메뉴번호
========================='''
def menu_select():
    print("1.추가 2.삭제 3.조회 4.전체조회 5.전체삭제 6.종료 7.파일읽기 8.파일저장")
    no = int(input("메뉴선택:"))
    return no

'''======================
회원등록
매개변수 : 회원정보 딕셔너리 {'userno':100,'username':'김동배','salary':2000}
리턴값: 없음
========================='''
def user_insert():
    info={ }
    info["userno"] = int(input("번호입력:"))
    info["username"] = input("이름입력:")
    info["salary"] = int(input("급여입력:"))
    return info
    
'''===================
회원삭제
매개변수 :삭제할 회원번호
리턴값:없음
===================='''
def user_delete(userno):
    
    idx = 0
    for i in users:
        if i["userno"] == userno:
            del users[idx]
            break
        idx +=1
'''========================
회원번호선택
매개변수: 보여줄 회원번호
리턴값 :
'''
def user_select(userno):
    
    for i in users:
        if i["userno"] == userno:
            print(i['username'],i['salary'])

'''=========================
전체조회
매개변수:회원정보
리턴값:
=================='''
def user_select_all():
    print("전체조회")
    for a in users:
        print(a['userno'],a['username'],a['salary'])

'''===============
종료

==============='''

def user_delete_all():
    users.clear()

users = [{'userno':100,'username':'김동배','salary':2000},
         {'userno':101,'username':'곽춘삼','salary':1000},
         {'userno':102,'username':'최봉팔','salary':1500}]

while True:
    #메뉴 선택
    no = menu_select()

    #유저 등록
    if no ==1:
        info = user_insert()   
        users.append(info)

    #유저 삭제
    elif no ==2:
        userno = int(input("삭제할 번호:"))
        user_delete(userno)

    #유저 조회
    elif no ==3:
        userno = int(input("조회할 번호:"))
        user_select(userno)
        
    #전체 조회
    elif no ==4:
        user_select_all()

    #전체삭제
    elif no ==5:
        user_delete_all()

    #종료
    elif no ==6 :
        break
print("The End")