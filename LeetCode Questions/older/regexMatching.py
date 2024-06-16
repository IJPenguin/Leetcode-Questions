s = "aab"
p = "c*a*b"
s_arr, p_arr = [*s] , [*p]
ans = True
i = index = 0

def checker(s, p , i , index, ans):
    if '*' not in p and '.' not in p:
        return p == s

    if i >= len(p) or index >= len(s):
        return ans
    
    if p[i] == '.':
        i += 1
        index += 1
        ans = True
        ans = checker(s, p , i , index, ans)
        return ans
    
    if p[i] == '*':
        i += 1
        if i == len(p):
            return True
        for _ in range(index, len(s)):
            if s[_] == p[i]:
                index = _
                ans = True
                ans = checker(s, p , i , index, ans)
                return ans
        return False
    
    if p[i] == s[i]:
        i += 1
        index += 1
        ans = True
        ans = checker(s, p , i , index, ans)
        return ans
    
print(checker(s, p , i, index, ans))


# def isMatch(self, s: str, p: str) -> bool:
#         dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]


#         dp[0][0] = True


#         for j in range(1, len(p) + 1):
#             if p[j - 1] == '*':
#                 dp[0][j] = dp[0][j - 2]


#         for i in range(1, len(s) + 1):
#             for j in range(1, len(p) + 1):
#                 if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
#                     dp[i][j] = dp[i - 1][j - 1]
#                 elif p[j - 1] == '*':
#                     dp[i][j] = dp[i][j - 2]  
#                     if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
#                         dp[i][j] |= dp[i - 1][j]


#         return dp[len(s)][len(p)]