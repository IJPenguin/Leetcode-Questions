def findMessages(N, A):
    letters = "abcdefghijklmnopqrstuvwxyz"
    r_letters = {letters[i]: letters[25 - i] for i in range(26)}

    seen = set()
    A_set = set(A)
    res = 0

    for word in A:
        if word not in seen:
            enc = "".join(r_letters[c] for c in word)
            if enc in A_set and enc != word:
                res += 1
                seen.add(word)
                seen.add(enc)
            else:
                res += 1
                seen.add(word)

    return res


N = 5
A = ["aaa", "hack", "zzz", "abcd", "szxp"]
