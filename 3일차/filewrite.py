
users = [{'userno':100,'username':'김동배','salary':2000},
         {'userno':101,'username':'곽춘삼','salary':1000},
         {'userno':102,'username':'최봉팔','salary':1500}]

#파일 오픈
file = open('basic.txt','w')
#쓰기
for el in users:
    file.write(f"{el['userno']} {el['username']} {el['salary']}\n")
#닫기
file.close()
