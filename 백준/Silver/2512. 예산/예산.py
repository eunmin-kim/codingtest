n = int(input())
jibang = list(map(int, input().split()))
budget = int(input())

def cal_mid(mid):
    total = 0
    for i in jibang:
        if i <= mid:
            total += i
        else:
            total += mid
    return total


low = 0
high = max(jibang)
answer = -1

while low <= high:
    mid = (low + high) // 2
    
    if cal_mid(mid) <= budget:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)