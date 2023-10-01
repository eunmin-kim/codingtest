n,m = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(m):
    a , b, c = map(int,input().split())
    if a == 1:
        nums[b-1] = c
    elif a == 2:
        for j in range(b,c+1):
            if nums[j-1] == 0:
                nums[j-1] = 1
            else:
                nums[j-1] = 0
    elif a == 3:
        for j in range(b,c+1):
            nums[j-1] = 0
    else:
        for j in range(b,c+1):
            nums[j-1] = 1
for i in nums:
    print(i,end=" ")