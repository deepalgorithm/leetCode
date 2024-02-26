import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(y, x):
    global visited, map_
    visited[y][x] = True

    if map_[y][x] == '-' and map_[y][x+1] == '-':
        dfs(y, x + 1)
    elif map_[y][x] == '|' and map_[y+1][x] == '|':
        dfs(y+1, x)


N, M = map(int, input().split())
MAX = 50 + 10
map_ = [[''] * MAX for _ in range(MAX)]
visited = [[False] * MAX for _ in range(MAX)]
answer = 0

# 1. map에 연결 정보 채우기
for i in range(1, N+1):
    line = input()
    for j in range(1, M + 1):
        map_[i][j] = line[j -1]

# 2. dfs 호출
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if not visited[i][j]:
            dfs(i, j)
            answer += 1

# 3. 정답 출력
print(answer)