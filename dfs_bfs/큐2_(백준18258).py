# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
from collections import deque
import sys

n = int(input())
d = deque([])

for i in range(n):
    command = sys.stdin.readline()
    command = command.split()

    if command[0] == "push":
        d.append(command[1])
    if command[0] == "pop":
        if len(d) == 0:
            print("-1")
        else:
            print(d.popleft())
    if command[0] == "size":
        print(len(d))
    if command[0] == "empty":
        if len(d) == 0:
            print("1")
        else:
            print("0")
    if command[0] == "front":
        if len(d) == 0:
            print("-1")
        else:
            print(d[0])
    if command[0] == "back":
        if len(d) == 0:
            print("-1")
        else:
            print(d[-1])