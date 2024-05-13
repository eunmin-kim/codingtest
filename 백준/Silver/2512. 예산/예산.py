n = int(input())
jibang = list(map(int, input().split()))
total_budget = int(input())

def calculate_budget(upper_bound):
    total_allocated = 0
    for budget in jibang:
        if budget > upper_bound:
            total_allocated += upper_bound
        else:
            total_allocated += budget
    return total_allocated

low = 0
high = max(jibang)
answer = 0

while low <= high:
    mid = (low + high) // 2
    if calculate_budget(mid) <= total_budget:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)
