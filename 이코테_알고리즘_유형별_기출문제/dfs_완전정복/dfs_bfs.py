import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx):
    global visited, graph

    visited[idx] = True
    print(idx, end=' ')

    for i in range(1, N+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)

def bfs():
    queue = []
    queue.append(V)
    visited[V] = True

    while queue:
        idx = queue.pop(0)
        print(idx, end = ' ')

        for i in range(1, N +1):
            if not visited[i] and graph[idx][i]:
                queue.append(i)
                visited[i] = True


N,M,V = map(int, input().split())

MAX = 1000+10
visited = [False] * MAX
graph = [[False] * MAX for _ in range(MAX)]

for _ in range(M):
    x , y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

dfs(V)
print()


visited = [False] * MAX
bfs()