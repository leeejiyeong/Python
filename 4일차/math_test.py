import math as m    #as를 붙여서 별칭으로 쓰기 가능(math -> m)

from math import ceil, floor    #from을 사용하면 import로 함수 이름을 미리 적어놔서 밑에서쓸때 모듈이름(math)를 안써도된다.

a = 4.6
print(floor(a))
print(ceil(a))     #math모듈

print(round(a))     #내장함수