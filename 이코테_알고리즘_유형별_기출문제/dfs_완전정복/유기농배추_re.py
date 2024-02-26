import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 함수
dirY = [-1, 1, 0, 0]
dirX = [0, 0 ,-1, 1]
def dfs(y, x):
    global graph
    graph[y][x] = False
    
    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if graph[newY][newX]:
            dfs(newY, newX)

# 0.입력 조건 설정 
T = int(input())
MAX = 50 + 10

# 1. map 정보 받기
while T > 0:
    T -= 1
    N, M, K =map(int, input().split())
    graph = [[False] * MAX for _ in range(MAX)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y + 1][x + 1] = True
    # 2. dfs 실행
    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if graph[i][j]:
                dfs(i, j)
                answer += 1
    # 3. 출력
    print(answer)