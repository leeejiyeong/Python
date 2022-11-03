'''
매개변수 함수를 전달하고자 할때 함수선언을 람다식으롭표현
'''

def print_hi():
    print("hi")
def print_hello():
    print("안녕하세요")

def call_10(func):
    for i in range(10):
        func()

call_10(print_hello)    #안에 함수에 ()있으면 안됨
call_10(lambda  : print("hi"))   
