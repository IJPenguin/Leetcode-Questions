arr = ["geeksforgeeks", "geeks", "geezer", "geek"]
# arr = ["abcdef", "abcdef", "abcdefg", "ab", "abc"]
res = ""
for i, char in enumerate(arr[0]):
    found = True
    for j, el in enumerate(arr):
        if i >= len(el) or char != el[i]:
            found = False
            break

    if not found:
        break
    res += char

print(res)