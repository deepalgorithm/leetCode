from queue import PriorityQueue

N, M = list(map(int, input().split()))

graph = [[] for _ in range(N)]
connect = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    graph[a -1].append(b - 1)
    connect[b - 1] += 1


# 위상 정렬
pq = PriorityQueue()

for i in range(N):
    if connect[i] == 0:
        pq.put(i)

learn = []
while pq.qsize() != 0:
    u = pq.get()

    learn.append(u)

    for v in graph[u]:
        connect[v] -= 1
        if connect[v] == 0:
            pq.put(v)

for i in range(N):
    print(learn[i] + 1, end = " ")