'''
딕셔너리(=객체)사용법
'''
info = {}

#이름입력
info["name"] = input("이름입력:")
#나이입력
info["age"] = input("나이입력:")
#주소입력
info["addr"] = input("주소입력:")

#info출력
for key in info:
    print(f"\n{key}\t{info[key]}")


# #주소지우기
# del info["addr"]
# print(info)

