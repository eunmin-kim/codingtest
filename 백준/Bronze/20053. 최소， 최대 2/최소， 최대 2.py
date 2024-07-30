T = int(input())
ans = []
for i in range(T):
    n = int(input())
    for i in range(1):
        nums = list(map(int, input().split()))
        ans.append([min(nums),max(nums)])

for i in ans:
    for t in i:
        print(f"{t}",end=" ")
    print()