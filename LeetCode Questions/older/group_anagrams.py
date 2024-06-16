from collections import Counter

strs = ["eat", "tea", "tan", "ate", "nat", "bat", "bat"]

# # strs = ["",""]
# strs = ["rag","orr","err","bad","foe","ivy","tho","gem","len","cat","ron","ump","nev","cam","pen","dis","rob","tex","sin","col","buy","say","big","wed","eco","bet","fog","buy","san","kid","lox","sen","ani","mac","eta","wis","pot","sid","dot","ham","gay","oar","sid","had","paw","sod","sop"]

# res = []
# dic = []

# for el in strs:
#     a = Counter(el)
#     found = False

#     for tup in dic:
#         key, val = tup

#         if key == a:
#             val.append(el)
#             found = True
#             break

#     if not found:
#         dic.append((a, [el]))

# for arr in dic:
#     k, v = arr
#     res.append(v)

# print(res)

d = {}
for s in strs:

    k = [0] * 26

    for c in s:
        k[ord(c) - ord("a")] += 1
    k = tuple(k)
    if k in d.keys():
        d[k].append(s)
    else:
        d[k] = [s]
print(list(d.values()))
