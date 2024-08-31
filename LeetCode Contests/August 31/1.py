num1 = 987
num2 = 879
num3 = 798

def leftPad(num, l):
    n = len(str(num))
    return "0" * (l - n) + str(num)        

def generateKey(num1, num2, num3):

    num1 = leftPad(num1, 4)
    num2 = leftPad(num2, 4)
    num3 = leftPad(num3, 4)
    res = ""
    for i in range(4):
        res += str(min([int(num1[i]), int(num2[i]), int(num3[i])]))
    return int(res)

print(generateKey(num1, num2, num3))