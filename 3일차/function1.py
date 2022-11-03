'''
p.275
'''
#함수선언
def hello_3_times(greeting, n=2):
    for i in range(n):
        print(greeting, end=' ')

#함수호출
g = "안녕하세요"
n = 10
hello_3_times(g,n)
print(end=" ")
hello_3_times(n=3,greeting="hi")

print('alpha','mike','fixtrot', sep='-')
input()