s = "srndawsjtkfjvkgrfqkovajfbvlhqpoxzmtffmlrwwevtixyksauepdilfyuabdundhlkrbmmeppxslyhnumekdqcsqpmlcjsyctqebxsbvpapbmlqhrddpdthaboqokljnlbtyaqpumlzncdjqazugsinxwhcmxvtuiclmjqcsbabuxadnivdvvrvxygxlrrlummxlnasjrkqbhtuutiakfkwmfbtoxqbzhhvdlkylxrtcfqgwhcxotklbvfpjmeshlxfzookpharvrgqmwodlhrwcoxgbkpkvxbdffczbqnjfvxyvijoiguvfjmadjphaworbwgmwiitphnaavpuywxepfdbygkbjiupvvpkdjfipjvrdtufofdyvzsecreyylsmxemucryrstlittgqpxaeurnxukramvoxfdqqtnwrmnxdxgcxwfsewgqbfoqjc"
# s = "aababbb"

if len(s) == 0 or len(s) == 1:
    print(0)

maxm = 0

for i in range(len(s)):
    left = i
    right = left + 1
    while right <= len(s):
        dic = {}
        for j in range(left, right):
            if s[j] not in dic:
                dic[s[j]] = 1
            else:
                dic[s[j]] += 1
        variance = max(dic.values()) - min(dic.values())
        maxm = max(maxm, variance)
        right += 1

print(maxm)
