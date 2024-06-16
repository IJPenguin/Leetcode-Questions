from collections import Counter
s = 'loveleetcode'
cnt = Counter(s)
for i, char in enumerate(s):
    if cnt[char] == 1:
        print(i)
