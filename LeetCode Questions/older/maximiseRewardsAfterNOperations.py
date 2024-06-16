rewardValues = [3, 6, 1, 2, 4]
# rewardValues = [1, 1, 3, 3]
rewardValues = [2, 15, 14, 18]


rewardValues.sort()
s = []
lookup = {}
n = len(rewardValues)

def solve(num, ind):
    a = [num] * (n - ind) 
    c = True

    while True:
        for i in range(ind + 1, n):
            val = rewardValues[i]
            for j, t in enumerate(a):
                if val > t:
                    a[j] += val
                    c = False
        if c:
            break    
        c = True
    print(a)

solve(2, 0)