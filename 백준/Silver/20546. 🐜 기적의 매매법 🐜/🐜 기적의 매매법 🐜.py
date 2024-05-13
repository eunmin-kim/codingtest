# 입력 받기
initial_money = int(input())
stock_prices = list(map(int, input().split()))

# 준현이 전략 (BNP)
jun_money = initial_money
jun_stocks = 0
for price in stock_prices:
    if jun_money >= price:
        jun_stocks += jun_money // price
        jun_money %= price

# 성민이 전략 (TIMING)
sung_money = initial_money
sung_stocks = 0
up_days = 0
down_days = 0
for i in range(1, len(stock_prices)):
    if stock_prices[i] > stock_prices[i-1]:
        up_days += 1
        down_days = 0
    elif stock_prices[i] < stock_prices[i-1]:
        down_days += 1
        up_days = 0
    else:
        up_days = 0
        down_days = 0
    
    # 3일 연속 상승 후 다음 날 매도
    if up_days == 3:
        sung_money += sung_stocks * stock_prices[i]
        sung_stocks = 0
        up_days = 0  # 매도 후 상승 카운트 초기화
    # 3일 연속 하락 후 다음 날 매수
    elif down_days == 3:
        if sung_money >= stock_prices[i]:
            sung_stocks += sung_money // stock_prices[i]
            sung_money %= stock_prices[i]
        down_days = 0  # 매수 후 하락 카운트 초기화

# 마지막 날 자산 계산
last_price = stock_prices[-1]
jun_final_assets = jun_money + jun_stocks * last_price
sung_final_assets = sung_money + sung_stocks * last_price

# 결과 출력
if jun_final_assets > sung_final_assets:
    print("BNP")
elif sung_final_assets > jun_final_assets:
    print("TIMING")
else:
    print("SAMESAME")
