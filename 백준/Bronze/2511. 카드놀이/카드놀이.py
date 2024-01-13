A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt_A = 0
cnt_B = 0
d = 0
last_win = ""
for i in range(10):
    if A[i] > B[i]:
        cnt_A += 3
        last_win = 'A'
    elif B[i] > A[i]:
        cnt_B += 3
        last_win = 'B'
    else:
        cnt_A += 1
        cnt_B += 1
        d += 1
if cnt_A == cnt_B and d != cnt_A:
    print(f"{cnt_A} {cnt_B}")
    print(f"{last_win}")
if cnt_A > cnt_B:
    print(f"{cnt_A} {cnt_B}")
    print("A")
if cnt_A < cnt_B:
    print(f"{cnt_A} {cnt_B}")
    print("B")
if cnt_A == cnt_B and d == cnt_A:
    print(f"{cnt_A} {cnt_B}")
    print("D")
