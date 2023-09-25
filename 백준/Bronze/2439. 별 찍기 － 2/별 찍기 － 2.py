import sys
N = int(sys.stdin.readline())
i = 1
for i in range(N):
    i += 1
    print(str('*'*i).rjust(N))