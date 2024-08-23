def max_energy_boost(energyDrinkA, energyDrinkB):
    n = len(energyDrinkA)

    dpA = [0] * n
    dpB = [0] * n

    dpA[0] = energyDrinkA[0]
    dpB[0] = energyDrinkB[0]

    for i in range(1, n):
        dpA[i] = max(dpA[i-1] + energyDrinkA[i], dpB[i-2] +
                     energyDrinkA[i] if i-2 >= 0 else energyDrinkA[i])
        dpB[i] = max(dpB[i-1] + energyDrinkB[i], dpA[i-2] +
                     energyDrinkB[i] if i-2 >= 0 else energyDrinkB[i])

    return max(dpA[-1], dpB[-1])


# Example usage:
energyDrinkA = [3, 1, 1]
energyDrinkB = [1, 3, 1]
print(max_energy_boost(energyDrinkA, energyDrinkB))  # Output: 7
