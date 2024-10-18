import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

connect = [0] * N
answer = []

for _ in range(M):
    a, b = list(map(int, input().split()))
    graph[a - 1].append(b - 1)
    connect[b - 1] += 1

#위상정렬
queue = deque([]) #수강가능한목록
for i in range(N):
    if connect[i] == 0:
        queue.append(i)


while len(queue) != 0:
    u = queue.popleft()
    answer.append(u)

    for v in graph[u]:
        connect[v] -= 1
        if connect[v] == 0:
            queue.append(v)

for i in range(N):
    print(answer[i] + 1, end=" ")