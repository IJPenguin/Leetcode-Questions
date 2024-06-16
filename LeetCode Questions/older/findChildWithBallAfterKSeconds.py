n = 3
k = 5   

b = 0  
rev = False  

for _ in range(k):
    if not rev:  
        b += 1
        if b == n - 1:  
            rev = True  
    else: 
        b -= 1
        if b == 0: 
            rev = False  
print(b)
