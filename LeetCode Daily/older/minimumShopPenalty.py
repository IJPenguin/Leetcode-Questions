customers = "YYNY"
penalty = [0 for _ in range(len(customers)+1) ]
for i in range(len(customers) + 1):
    for j in range(len(customers)):
        if j < i:
            if customers[j] == 'Y':
                continue
            else:
                penalty[i] += 1
        else:
            if customers[j] == 'Y':
                penalty[i] += 1
            else:
                continue


print(penalty.index(min(penalty)))