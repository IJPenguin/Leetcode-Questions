# strs = ["neet", "code", "love", "you"]
strs = ["we","say",":","yes","!@#$%^&*()"]

def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "_"  + s
    return res

def decode(s):
    i = 0
    res = []
    while i < len(s):
        num = ""
        while True:
            if s[i] == "_":
                break
            else:
                num += s[i]
            i += 1
        num = int(num)
        res.append(s[i: i + num])
        i += num
    return res 

t = encode(strs)
print(t)
print(decode(t))