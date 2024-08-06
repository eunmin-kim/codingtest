N = int(input())
cows = {}
cnt = 0
for i in range(N):
    cow, direct = map(int, input().split())
    if cow not in cows:
        cows[cow] = direct
    else:
        if cows[cow] != direct:
            cnt += 1
            cows[cow] = direct
    
print(cnt)