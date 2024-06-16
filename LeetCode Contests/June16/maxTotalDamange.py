from typing import List
from collections import defaultdict

class Solution:
    def maximumTotalDamage(self, powers: List[int]) -> int:
        damage_frequency = defaultdict(int)
        for power in powers:
            damage_frequency[power] += 1
        
        unique_powers = sorted(damage_frequency.keys())
        
        unique_count = len(unique_powers)
        if unique_count == 1:
            return unique_powers[0] * damage_frequency[unique_powers[0]]
        
        max_damage = [0] * (unique_count + 1)
        
        for i in range(1, unique_count + 1):
            current_damage = unique_powers[i - 1] * damage_frequency[unique_powers[i - 1]]
            take_damage = current_damage

            for j in range(i - 2, -1, -1):
                if unique_powers[i - 1] - unique_powers[j] > 2:
                    take_damage += max_damage[j + 1]
                    break
            
            dont_take_damage = max_damage[i - 1]
            max_damage[i] = max(take_damage, dont_take_damage)
        
        return max_damage[unique_count]

# Example usage:
solution = Solution()
powers = [3, 4, 2, 3, 1, 2]
print(solution.maximumTotalDamage(powers))  # Example output