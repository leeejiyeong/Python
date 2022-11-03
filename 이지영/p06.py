cod = input("사원번호입력:")

if cod[2:5] == "A01":
    print("부서:인사")
elif cod[2:5] == "B02":
    print("부서:개발")
elif cod[2:5] == "A02":
    print("부서:총무")
