import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

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
        map_[i][j] = row(j -1)
# 2. dfs 실행

# 3. 출력