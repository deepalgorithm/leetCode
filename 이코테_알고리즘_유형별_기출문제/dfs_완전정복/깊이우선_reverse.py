import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 함수
def dfs(idx):
    global visited, answer, order, graph
    visited[idx] = True
    answer[idx] = order
    order += 1
    for i in graph[idx]:
        if not visited[i]:
            dfs(i)

#0. 입력정보받기
N, M, R = map(int, input().split())
MAX = 100_000 + 10
visited = [False] * MAX
answer = [0] * MAX
order = 1
graph = [[] for _ in range(N+1)]

#1. 그래프 정보 입력받기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
#2. 내림차순 정렬
for i in range(1, N + 1):
    graph[i].sort(reverse =True)

#3. dfs
dfs(R)
#4. 출력
for i in range(1, N+1):
    print(answer[i])