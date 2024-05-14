# 초기 방향은 북쪽(N)을 바라보고 있음
a = 0

# 10개의 명령을 입력 받음
for i in range(10):
    b = int(input())
    c = 0
    if b == 1:      # 우향우 (오른쪽 90도 회전)
        c = 90
    elif b == 2:    # 뒤로 돌아 (오른쪽 180도 회전)
        c = 180
    elif b == 3:    # 좌향좌 (왼쪽 90도 회전)
        c = -90
    a += c

# a 값을 360도로 나눈 나머지 값을 구함 (방향을 0도 ~ 359도로 변환)
a %= 360

# 각도에 따라 방향 출력
if a == 90:
    print("E")
elif a == 180:
    print("S")
elif a == 270:
    print("W")
else:  # a == 0
    print("N")
