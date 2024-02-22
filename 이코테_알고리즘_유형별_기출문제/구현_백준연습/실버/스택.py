from collections import deque
import sys

N = int(sys.stdin.readline())
dq = deque()

for _ in range(0, N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        dq.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'top':
        if len(dq)==0:
            print(-1)
        else:
            print(dq[-1])