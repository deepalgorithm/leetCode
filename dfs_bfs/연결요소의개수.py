import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx):
    global graph, visited
    visited[idx] = True

    for i in range(1, N + 1):
        if not visited[i] and graph[idx][i]:
            dfs(i)

# 0. 입력초기화
MAX = 1000 + 10
N, M = map(int, input().split())
graph = [[False] * MAX for _ in range(MAX)]
visited = [False] * MAX
answer = 0

# 1. graph에 연결 정보 채우기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = True
    graph[v][u] = True

# 2. DFS 호출
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        answer += 1
# 3. 출력
print(answer)