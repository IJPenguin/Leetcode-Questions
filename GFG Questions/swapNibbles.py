n = 100
n = str(bin(100))[2:]
n = n.zfill(8)
n = n[-4:] + n[:4]
n = int(n, 2)
print(n)