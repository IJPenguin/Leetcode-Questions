import random


class Codec:

    def __init__(self):
        self.hash = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        base = "http://tinyurl.com/"
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        while True:
            temp = base
            for i in range(6):
                temp += random.choice(chars)
            if temp not in self.hash:
                base = temp
                self.hash[temp] = longUrl
                break
        return base

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hash[shortUrl]


url = "https://leetcode.com/problems/design-tinyurl"
s = Codec()
short = s.encode(url)
print(short)
print(s.decode(short))
