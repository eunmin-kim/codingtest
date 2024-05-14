n = int(input())
jibang = list(map(int, input().split()))
budget = int(input())

def cal_budget(mid):
    total = 0
    for i in jibang:
        if i > mid:
            total += mid
        else:
            total += i
    return total


min_n = 0
max_n = max(jibang)
answer = -1

while min_n <= max_n:
    mid = (max_n + min_n) // 2
    
    if cal_budget(mid) <= budget:
        answer = mid
        min_n = mid + 1
    else:
        max_n = mid - 1
print(answer)