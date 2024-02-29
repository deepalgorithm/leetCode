import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx):
    global graph, visited, answer
    visited[idx] = True
    answer += 1

    for i in range(1, N+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)


N  = int(input())
M = int(input())
MAX = 100 + 10
graph = [[False] * MAX for _ in range(MAX)]
visited = [False] * MAX
answer = 0

for _ in range(M):
    x,y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

dfs(1)

print(answer -1)