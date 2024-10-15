import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

def dfs(idx):
    global visited, graph, count
    visited[idx] = True

    for v in graph[idx]:
        if not visited[v]:
            dfs(v)

N = int(input())
M = int(input())

graph = [[] for _ in range(N)]
count = 0 
visited = [False] * N


for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

dfs(0)
for i in range(1,N):
    if visited[i]:
        count += 1

print(count)