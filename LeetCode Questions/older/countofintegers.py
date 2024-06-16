num1 = "1"
num2 = "12"
min_num = 1
max_num = 8

a = int(num1)
b = int(num2)

count = 0
e = 10**9 + 7
for i in range(a, b+1):
    digit_sum = 0
    for digit in str(i): 
        digit_sum += int(digit)

    if digit_sum >= min_num and digit_sum <= max_num:
        count += 1

print (count%e)

