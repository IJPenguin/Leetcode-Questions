def count_k_constraint_substrings(s, k):
    n = len(s)
    count = 0
    
    for i in range(n):
        zeros = 0
        ones = 0
        
        for j in range(i, n):
            if s[j] == '0':
                zeros += 1
            else:
                ones += 1
            
            if zeros <= k or ones <= k:
                count += 1
            else:
                break  
    
    return count

