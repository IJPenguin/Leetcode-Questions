class Solution:
    def winningPlayerCount(self, n, pick) -> int:
        counts = {i: {} for i in range(n)}
        
        for x, y in pick:
            if y not in counts[x]:
                counts[x][y] = 0
            counts[x][y] += 1
        
        winners = 0
        for player, color_counts in counts.items():
            if any(count > player for count in color_counts.values()):
                winners += 1
                
        return winners