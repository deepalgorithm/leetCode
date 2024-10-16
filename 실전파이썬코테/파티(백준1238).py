import sys
input = sys.stdin.readline
from queue import PriorityQueue

N, M, X = list(map(int, input().split()))
X -= 1

graph = [[] for _ in range(N)]
reverse_graph = [[] for _ in range(N)]


for _ in range(M):
    u, v, w = list(map(int, input().split()))
    graph[u - 1].append((v - 1, w))
    reverse_graph[v - 1].append((u - 1, w))

#원래 그래프에서 다익스트라
dist = [1e9] * N
queue = PriorityQueue()

dist[X] = 0
queue.put((0, X))

while queue.qsize() != 0:
    d, u = queue.get()

    if d != dist[u]:
        continue

    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            queue.put((dist[v], v))

# 역 그래프에서 다익스트라
reverse_dist = [1e9] * N
reverse_queue = PriorityQueue()

reverse_dist[X] = 0
reverse_queue.put((0, X))

while reverse_queue.qsize() != 0:
    d, u = reverse_queue.get()

    if d != reverse_dist[u]:
        continue

    for v ,w in reverse_graph[u]:
        if reverse_dist[v] > reverse_dist[u] + w:
            reverse_dist[v] = reverse_dist[u] + w
            reverse_queue.put((reverse_dist[v], v))

max_dist = 0

for i in range(N):
    if max_dist < dist[i] + reverse_dist[i]:
        max_dist = dist[i] + reverse_dist[i]

print(max_dist)