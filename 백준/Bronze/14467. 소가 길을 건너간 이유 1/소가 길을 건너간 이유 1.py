n = int(input())

cows= {}
cnt = 0
for i in range(n):
    cow, direct = map(int, input().split())
    if cow not in cows:
        cows[cow] = direct
    else:
        if cows[cow] != direct:
            cnt += 1
            cows[cow] = direct
        else:
            continue
print(cnt)