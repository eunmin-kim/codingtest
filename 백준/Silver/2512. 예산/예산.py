n = int(input())
jibang = list(map(int, input().split()))
budget = int(input())
min_n = 0
max_n = max(jibang)

good_upper_bound = -1

def calculate_needed_budget(upper_bound):
    
    needed_budget = 0
    for money in jibang:
        needed_budget += min(money, upper_bound)
    return needed_budget

while min_n <= max_n:
    mid = (min_n + max_n) // 2
    
    if calculate_needed_budget(mid) <= budget:
        good_upper_bound = mid
        min_n = mid + 1
    else:
        max_n = mid - 1

answer = -1
for i in jibang:
    given = min(i, good_upper_bound)
    answer = max(answer,given)
print(answer)