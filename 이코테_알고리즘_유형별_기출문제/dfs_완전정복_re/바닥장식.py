import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#가로 또는 세로만 확인
def dfs(y,x):
    global map_, visited
    visited[y][x] = True

    if map_[y][x] == '-' and map_[y][x + 1] == '-':
        dfs(y, x + 1)
    elif map_[y][x] == '|' and map_[y+1][x] == '|':
        dfs(y + 1, x)



# 0. 입력 조건 설정
N, M = map(int, input().split())
MAX = 50 + 10
map_ = [[''] * MAX for _ in range(MAX)]
visited = [[False] * MAX for _ in range(MAX)]
answer = 0

# 1. map 정보 입력 받기
for i in range(1, N + 1):
    row = input()
    for j in range(1, M + 1):
        map_[i][j] = row[j-1]
# 2. dfs 실행
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if not visited[i][j]:
            dfs(i, j)
            answer += 1
# 3. 출력
print(answer)