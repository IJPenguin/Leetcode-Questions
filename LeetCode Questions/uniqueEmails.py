from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        d = {}

        for email in emails:
            at = email.index("@")
            domain = email[at + 1:]
            local = email[: at]
            effective = ""

            for char in local:
                if char == ".":
                    continue
                elif char == "+":
                    break
                else:
                    effective += char

            if domain in d:
                d[domain].add(effective)
            else:
                d[domain] = set()
                d[domain].add(effective) 

        res = 0
        for s in d.values():
            res += len(s)
        return res



emails = ["test.email+alex@leetcode.com",
          "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
s = Solution()
print(s.numUniqueEmails(emails))
