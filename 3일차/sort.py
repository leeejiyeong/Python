arr = [2,0,17,45,21,38,26]
arr.sort(reverse = True)
print(arr)

users = [{'userno':100,'username':'김동배','salary':2000},
         {'userno':101,'username':'곽춘삼','salary':1000},
         {'userno':102,'username':'최봉팔','salary':1500}]

users.sort(key=lambda item : item['salary'],reverse=True)
print(users)