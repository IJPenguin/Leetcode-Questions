# s = "abcd"
# k = 2

s = "mxz" 
k = 3

def stringHash(s, k):
    result = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"

    for i in range(0, len(s), k):
        t = ""

        for j in range(k):
            t += s[i + j]

        temp = 0

        for char in t:
            temp += alpha.index(char)
        result += alpha[temp % 26]

    return result


print(stringHash(s, k))
