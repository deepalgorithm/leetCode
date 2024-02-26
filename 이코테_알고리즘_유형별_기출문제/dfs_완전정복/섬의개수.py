import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# dirY = [-1, 1, 0, 0]
# dirX = [0, 0, -1, 1]
#위, 위 오른쪽, 오른쪽, 오른쪽 아래, 아래, 아래 왼쪽, 왼쪽, 왼쪽 위
dirY = [-1,-1, 0, 1, 1, 1, 0, -1]
dirX = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(y,x):
    global map_, visited
    visited[y][x] = True

    for i in range(8):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if map_[newY][newX] and not visited[newY][newX]:
            dfs(newY, newX)


while True:
    M, N = map(int, input().split())
    MAX = 50 + 10

    if N == 0 and M == 0:
        break
    # 1. map에 연결 정보 채우기
    map_ = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]
    
    for i in range(1, N + 1):
        row = list(map(int, input().split()))
        for j in range(1, M + 1):
            map_[i][j] = (row[j - 1] == 1)

    # 2. dfs 호출
    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if map_[i][j] and not visited[i][j]:
                dfs(i, j)
                answer += 1

    #정답 출력
    print(answer)