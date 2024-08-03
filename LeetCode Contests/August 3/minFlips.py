class Solution:
    def minFlips(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        
        def flips_to_make_palindromic(array):
            l = len(array)
            flips = 0
            for i in range(l // 2):
                if array[i] != array[l - i - 1]:
                    flips += 1
            return flips

        row_flips = sum(flips_to_make_palindromic(grid[i]) for i in range(m))
        column_flips = sum(flips_to_make_palindromic([grid[i][j] for i in range(m)]) for j in range(n))

        return min(row_flips, column_flips)