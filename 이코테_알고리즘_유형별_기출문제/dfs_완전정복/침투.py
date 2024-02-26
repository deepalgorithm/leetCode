import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [-1,1,0,0]
dirX = [0,0,-1,1]

def dfs(y,x):
    global visited, map_, answer, N
    visited[y][x] = True

    if y == N:
        answer = True
        return

    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if map_[newY][newX] and not visited[newY][newX]:
            dfs(newY, newX)

# 0. 입력 및 초기화
N, M = map(int, input().split())
MAX = 1000 + 10
map_ = [[False] * MAX for _ in range(MAX)] 
visited = [[False] * MAX for _ in range(MAX)] 

# 1. map에 연결정보 채우기
for i in range(1, N + 1):
    row = input()
    for j in range(1, M + 1):
        if row[j-1] == "0":
            map_[i][j] = True
        else:
            map_[i][j] = False
        
# 2. DFS 호출
answer = False
for j in range(1, M+1):
    if map_[1][j]:
        dfs(1, j)

# 3. 출력
print("YES" if answer else "NO") 