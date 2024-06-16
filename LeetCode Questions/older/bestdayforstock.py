prices = [7,1,5,3,6,4]

if not prices or len(prices) < 2:
    print(0)

max_profit = 0
min_price = prices[0]

for i in range(len(prices)):
    if prices[i] < min_price:
        min_price = prices[i]
    else:
        profit = prices[i] - min_price
        max_profit = max(profit, max_profit)

print(max_profit)