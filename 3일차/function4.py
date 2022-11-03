'''
가변 매개변수(*)
tuple : () -> list와 동일하지만 요소 변경 불가
list :  []
'''
'''
합계계산
매개변수 : 정수형 여러개 있음
리턴값 : 정수형 합계
'''
def mysum(*nums):
    total = 0
    for num in nums:
        total += num
    
    # print(type(nums))
    return total

t = mysum(10,20)
print(t)
print(mysum(10,20,30))
print(mysum(14,20,23,39,18,56,79))
print("합계",t)
