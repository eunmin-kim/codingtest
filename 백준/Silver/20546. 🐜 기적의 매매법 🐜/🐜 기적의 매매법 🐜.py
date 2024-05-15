amount = int(input())
stock_price = list(map(int, input().split()))
jun = amount
sungmin = amount

jun_stock = 0
sungmin_stock = 0
up = 0
down = 0
for i in range(len(stock_price)):
    jun_stock += jun // stock_price[i]
    jun = jun % stock_price[i]
for i in range(1,len(stock_price)):

    
    if stock_price[i-1] < stock_price[i]:
        up += 1
        down = 0
    elif stock_price[i-1] > stock_price[i]:
        down += 1
        up = 0
    else:
        up = 0
        down = 0
    
    
    
    
    # sell
    if up == 3:
        sungmin += stock_price[i] * sungmin_stock
        sungmin_stock = 0
        up = 0
    # buy
    if down == 3:
        if sungmin >= stock_price[i]:
            sungmin_stock += sungmin // stock_price[i]
            sungmin = sungmin - sungmin_stock * stock_price[i]
        down = 0

    
last_price = stock_price[len(stock_price)-1]

jun_last = last_price * jun_stock + jun
sung_last = last_price * sungmin_stock + sungmin

if jun_last > sung_last:
    print("BNP")
elif jun_last < sung_last:
    print("TIMING")
else:
    print("SAMESAME")