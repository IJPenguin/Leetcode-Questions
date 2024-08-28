class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            if f"{i}{i}{i}" in num:
                return f"{i}{i}{i}"
        return ""

num = "6777133339"
# num = "2300019"
# num = "42352338"
s = Solution()
print(s.largestGoodInteger(num))