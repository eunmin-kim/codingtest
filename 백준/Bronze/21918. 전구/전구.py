N, M = map(int, input().split())
status = list(map(int, input().split()))
commands = []
for i in range(M):
    command = list(map(int, input().split()))
    commands.append(command)


for j in range(len(commands)):
    if commands[j][0] == 1:
        status[commands[j][1]-1] = commands[j][2]
    if commands[j][0] == 2:
        for t in range(commands[j][1]-1,commands[j][2]):
            if status[t] == 0:
                status[t] = 1
            else:
                status[t] = 0
    if commands[j][0] == 3:
        for t in range(commands[j][1]-1,commands[j][2]):
            status[t] = 0
    if commands[j][0] == 4:
        for t in range(commands[j][1]-1,commands[j][2]):
            status[t] = 1
for i in status:
    print(i,end=" ")