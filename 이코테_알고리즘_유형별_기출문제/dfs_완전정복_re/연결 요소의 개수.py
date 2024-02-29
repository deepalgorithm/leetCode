import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(idx):
    global graph, visited
    visited[idx] = True

    for i in range(1, N + 1):
        if not visited[i] and graph[idx][i]:
            dfs(i)

N, M = map(int, input().split())
MAX = 1000 + 10
graph = [[False] * MAX for _ in range(MAX)]
visited = [False] * MAX
answer = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = True
    graph[v][u] = True

for i in range(1, N):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)