users = [{'userno':100,'username':'김동배','salary':2000},
         {'userno':101,'username':'곽춘삼','salary':1000},
         {'userno':102,'username':'최봉팔','salary':1500}]

arr = list(filter(lambda item : item['salary']>1000 ,users))
nos = list(map(lambda item : item['userno'],users))
print(nos)