# s = "abab"
s = "acccbaaacccbaac"
l = 0
r = 1
res = ""
templ = ""
tempr = ""
while r < len(s):
    templ += s[l]
    tempr += s[r]
    print(templ, tempr)
    

print(res)