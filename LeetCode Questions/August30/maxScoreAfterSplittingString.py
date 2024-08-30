class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeros = 0
        ans = 0 

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1
        
            ans = max(ans, zeros + ones)
        
        return ans
    
s1 = "011101"
s2 = "00111"
s3 = "1111"
s4 = "0100"
s = Solution()
print(s.maxScore(s1))       
print(s.maxScore(s2))       
print(s.maxScore(s3))       
print(s.maxScore(s4))