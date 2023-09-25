for i in range(3):
    a = 0
    n = int(input())
    for j in range(n):
        t = int(input())
        a += t
    if a == 0:
        print("0")
    elif a < 0:
        print("-")
    else:
        print("+")