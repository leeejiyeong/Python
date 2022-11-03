# class.py
# 클래스 = 데이터 +함수

class ClacClass:
    #맴버변수
    a=0
    b=0

    #생성자:객체생성시에 변수초기화
    def __init__(self,a,b):
        self.a = a
        self.b = b

    #맴버함수 = 메소드
    def add(self):  
        print(self.a+self.b)

    def miu(self):  
        print(self.a-self.b)

    def mul(self):  
        print(self.a*self.b)

    def div(self):  
        print(self.a/self.b)