s = "leetcoder"
# s = "bbcd"

def doesAliceWin(s):
    vowels = set("aeiou")
    s = [*s]
    turn = True # True means Alice
    while s:
        p = 0
        temp = 0
        num = 0
        while p < len(s):
            if s[p] in vowels:
                num += 1
                if num % 2 != 0 and turn:
                    temp = p
            elif num % 2 == 0 and not turn:
                temp = p
            p += 1
        s = s[temp + 1:]
        print(s)
    return turn       


print(doesAliceWin(s))