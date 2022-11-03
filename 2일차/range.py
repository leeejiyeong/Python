'''
특정한 횟수만큼 반복
'''

#1~10
# for i in range(11,0,-2):
#     #공백출력
#     print(" "*((11-i)//2) , "*"*i)


n=int(input())
for i in range(1,n+1):
    #공백출력
    for j in range(n-i):
        print("",end="")

    # 별 출력
    for j in range(i):
        print("*", end = "")
    print()

output = ""
for i in range(1,n+1):
    #공백출력
    for j in range(n-i):
        output += " "

    # 별 출력
    for j in range(i):
        output += "*"
    output += '\n'
print(output)
