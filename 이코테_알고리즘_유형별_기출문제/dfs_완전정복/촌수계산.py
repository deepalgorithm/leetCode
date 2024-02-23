import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#함수 생성
def dfs(idx, count):
    global graph, answer, visited, end
    visited[idx] = True
    if idx == end:
        answer = count
        return
    
    for i in range(1, n+1):
        if not visited[i] and graph[idx][i]:
            dfs(i, count +1)

# 0. 입력 조건 설정
n = int(input()) # 전체 사람의 수
start, end = map(int, input().split()) # 촌수를 계산해야 하는 서로 다른 두 사람
m = int(input()) # 간선의 개수
answer = -1
MAX = 100 + 10
visited = [False] * MAX
graph = [[False] * (n+1) for _ in range(n+1) ]

# 그래프 입력 받기
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

# dfs
dfs(start, 0)

# 정답 출력

print(answer)