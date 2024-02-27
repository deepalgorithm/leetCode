import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [0, 1]
dirX = [1, 0]

def dfs(y,x):
    global visited, map_
    visited[y][x] = True

    if y == N  and x == N:
        return

    for i in range(2):
        newY = y + dirY[i] * map_[y][x]
        newX = x + dirX[i] * map_[y][x]

        if not visited[newY][newX]:
            dfs(newY, newX)

# 0. 입력조건 받기
N = int(input())
MAX = 3 + 100 + 10 
map_ = [[0] * MAX for _ in range(MAX)]
visited = [[False] * MAX for _  in range(MAX)]
# 1. map 정보 입력 받기
for i in range(1, N +1):
    row = list(map(int, input().split()))
    for j in range(1, N + 1):
        map_[i][j] = row[j -1]

# 2. dfs 실행
dfs(1, 1)

# 3. 정답 출력

print("HaruHaru" if visited[N][N] else "Hing")