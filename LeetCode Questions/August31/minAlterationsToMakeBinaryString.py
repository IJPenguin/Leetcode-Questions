# class Solution:
#     def minOperations(self, s: str) -> int:
#         s = [*s]
#         n = len(s)
        
#         zero = ["0" if i%2 == 0 else "1" for i in range(n)]
#         one = ["1" if i%2 == 0 else "0" for i in range(n)]
#         s1 = 0
#         s2 = 0
#         for i in range(n):
#             if s[i] != zero[i]:
#                 s1 += 1
#             elif s[i] != one[i]:
#                 s2 += 1
#         return min(s1, s2)

class Solution:
    def minOperations(self, s: str) -> int:
        cnt1, cnt2 = 0, 0
        c1, c2 = '0', '1'
        for c in s:
            if c == c1:
                cnt2 += 1
            else:
                cnt1 += 1
            c1, c2 = c2, c1
        return min(cnt1, cnt2)

s1 = "0100"
s2 = "10"
s3 = "1111"
s4 = "10010100"
s = Solution()
print(s.minOperations(s1))
print(s.minOperations(s2))
print(s.minOperations(s3))
print(s.minOperations(s4))
