n = int(input())

for i in range(n):
    num = int(input())
    for j in range(2,1000001):
        if num % j == 0:
            print("NO")
            break
        if j == 1000000:
            print("YES")