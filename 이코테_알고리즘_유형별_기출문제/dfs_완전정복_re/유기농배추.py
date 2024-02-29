import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [-1, 1, 0, 0]
dirX = [0, 0, -1, 1]

def dfs(y,x):
    global graph, visited
    visited[y][x] = True

    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if not visited[newY][newX] and graph[newY][newX]:
            dfs(newY, newX)

T = int(input())
MAX = 50 + 10


while T > 0:
    T -= 1
    M, N, K = map(int, input().split())

    graph = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x + 1][y + 1] = True

    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if not visited[i][j] and graph[i][j]:
                dfs(i, j)
                answer += 1

    print(answer)