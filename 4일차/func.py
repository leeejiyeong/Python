
def mat_total(std):

    matSum = 0
    for score in std:
        matSum += score['mat']
    print(matSum)

std = [ {"mat":50, "eng":80},
        {"mat":40, "eng":70},
        {"mat":30, "eng":90}]

mat_total(std)