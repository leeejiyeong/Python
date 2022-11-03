'''
파이썬의 list == 자바스크립트의 array
배열에 요소 추가, 삭제, 조회, 변경
'''

arr=['김','이','박','옹']

#제일 마지막에 최씨 추가 (append)
arr.append("최")
#맨 처음에 강씨 추가 (insert)
arr.insert(0,"강")
#김씨를 빼기 (del)
del arr[1]
#박씨 빼기(remove)
arr.remove("박")

print(arr)