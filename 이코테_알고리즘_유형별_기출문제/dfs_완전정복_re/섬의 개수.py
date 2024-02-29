import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [-1, -1, 0, 1, 1, 1, 0, -1]
dirX = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(y, x):
    global visited, map_
    visited[y][x] = True

    for i in range(8):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if not visited[newY][newX] and map_[newY][newX]:
            dfs(newY, newX)


while True:
    M, N = map(int, input().split())
    MAX = 50 + 10

    if N == 0 and M == 0:
        break

    map_ = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]

    for i in range(1, N + 1):
        row = list(map(int, input().split()))
        for j in range(1, M +1):
            map_[i][j] = (row[j -1] == 1)

    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if map_[i][j] and not visited[i][j]:
                dfs(i, j)
                answer += 1

    print(answer)

