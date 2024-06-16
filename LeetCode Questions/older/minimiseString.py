s = "kkkkqdxre"
arr = [*s]
uniq = set(arr)
ans = []

def adder(ans, el, count):
    n = count // 3
    for _ in range(n):
        ans.append(el)
    if count%3 != 0:
        ans.append(el)
    return

for el in uniq:
    count = arr.count(el)
    adder(ans, el, count)
    
print(ans)