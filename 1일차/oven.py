'''
오븐시계 계산
'''

#현재시간 입력 (시, 분)
h,m = input().split(' ')

#요리시간 입력
s = input()

#정수형으로 변환
h = int(h)
m = int(m)
s = int(s)

#요리시간을 60으로 나눈 몫을 -> 시간에다가 더하기   //
h = h + (s // 60)  # h += (s // 60)

#요리시간을 60으로 나눈 나머지를 -> 분에다가 더하기    %
m = m + (s % 60)

#분을 60으로 나눈 몫을 시에다가 더하기
h = h + (m // 60)

#분을 60으로 나눈 나머지를 분에다가 더하기
m = (m % 60)

#출력
print(h,m)

#시간이 24시라면 0시로 변경


