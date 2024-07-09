import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#dfs
def dfs(idx):
    global graph, dfs_visited
    dfs_visited[idx] = True
    print(idx, end = ' ')

    for i in range(N + 1):
        if not dfs_visited[i] and graph[idx][i]:
            dfs(i)

# 0. 입력 및 초기화
N,M,V = map(int, input().split())
MAX = 1000 + 10
graph = [[False] * MAX for _ in range(MAX)]
dfs_visited = [False] * MAX
bfs_visited = [False] * MAX

# 1. graph에 연결 정보 채우기
for _ in range(M):
    x, y = map(int, input().split()) 
    graph[x][y] = True
    graph[y][x] = True
# 2. DFS 호출
dfs(V)
print()
# 3. BFS 호출
q = [V]
while q:
    cur = q.pop(0)
    bfs_visited[cur] = True
    print(cur, end=' ')
    for i in range(1, N+1):
        if not bfs_visited[i] and graph[cur][i]:
            bfs_visited[i] = True
            q.append(i)