n = 9
k = 4

def largest_k_palindromic(n, k):
    def is_palindrome(s):
        return s == s[::-1]

    def generate_palindromes(length):
        if length == 1:
            return [str(i) for i in range(1, 10)]
        half_length = (length + 1) // 2
        palindromes = []
        for i in range(10**(half_length - 1), 10**half_length):
            s = str(i)
            if length % 2 == 0:
                palindrome = s + s[::-1]
            else:
                palindrome = s + s[-2::-1]
            palindromes.append(palindrome)
        return palindromes

    palindromes = generate_palindromes(n)
    for p in reversed(palindromes):
        if int(p) % k == 0:
            return p


print(largest_k_palindromic(n, k))
