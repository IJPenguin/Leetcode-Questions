temperatures = [73,74,75,71,69,72,76,73]
res = [0] * len(temperatures)
stack = [] # pair : [t, i]

for i, t in enumerate(temperatures):
    while stack and t > stack[-1][0]:
        stackT, stackI = stack.pop()
        res[stackI] = i - stackI
    stack.append([t, i])

print(res)