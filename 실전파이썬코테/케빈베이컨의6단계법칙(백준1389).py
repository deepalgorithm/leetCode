from collections import deque

N, M = list(map(int, input().split()))

graph = [[] for _ in range(N)]

min_kevin_bacon = 1e9
min_person = -1

for _ in range(M):
    a, b = list(map(int, input().split()))

    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(N):
    #i를 시작점으로 하는 BFS
    # 각 노드까지의 최단거리를 구해서 다 합하기
    visited = [False] * N
    dist = [-1] * N

    queue = deque([i])
    visited[i] = True
    dist[i] = 0

    while len(queue) != 0:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                dist[v] = dist[u] + 1

    kevin_bacon = sum(dist)
    if min_kevin_bacon > kevin_bacon:
        min_kevin_bacon = kevin_bacon
        min_person = i

print(min_person + 1)