#open
with open('d:/pythonwork/3일차/basic.txt','r') as file:
    #한줄씩 처리
    lines = file.readlines()
    for line in lines:
        info = line.split(" ")
        print(info[1])

    #read
    txt = file.read()
    print(txt)
