'''
반복문
'''
#list
names = ['김','이','박']

print("list===")
for obj in names:
    print(obj)

#list range
print("list range====")
for idx in range(len(names)):
    print(names[idx])


#dictionary
dict = {'no':100, 'username':'user1','salary': 2000}

print("list=======")
for key in dict:
    print(key, dict[key])

print("dict=========")
for key, value in dict.items():
    print(key, value)


users = [{'no':100,'username':'user1','salary':2000},
         {'no':101,'username':'user2','salary':1000},
         {'no':102,'username':'user3','salary':1500}]

print("list dict==========")
for obj in users:
    print(obj['username'])

print("list dict range========")
for obj in range(len(users)):
    print(users[obj]["username"]) #list는 인덱스로 접근 dictionary는 키로 접근

#급여합계구하기
print("salary sum=======")
total = 0
for s in users:
    total += s['salary']
print("합계:", total)

#최대급여, 최소급여
maxSal = users[0]['salary']
minSal = users[0]['salary']

for m in users:
    if m['salary'] > maxSal:
        maxSal = m['salary']
    if m['salary'] < minSal:
        minSal = m['salary']
        
print("최대급여:", maxSal)
print("최소급여:", minSal)

