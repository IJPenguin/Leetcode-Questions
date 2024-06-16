import re
s = "A man, a plan, a canal: Panama"

def is_palindrome(s):
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]

print(is_palindrome(s))