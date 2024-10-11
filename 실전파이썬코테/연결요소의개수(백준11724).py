from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N) ]
answer = 0
visited = [False] * N

for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

for i in range(N):
    if visited[i]:
        continue
    #bfs를 시작
    answer += 1

    queue = deque([i])
    visited[i] = True

    while len(queue) != 0:
        u = queue.popleft()
        
        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True

print(answer)