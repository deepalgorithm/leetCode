import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx):
    global graph, visited, answer, order
    visited[idx] = True
    answer[idx] = order
    order += 1

    for i in graph[idx]:
        if not visited[i]:
            dfs(i)

# 0.입력 조건 받기
MAX = 100_000 + 10
N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * MAX
answer = [0] * MAX
order = 1
# 1. 그래프에 연결 정보 입력
for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 2. DFS
for i in range(1, N +1):
    graph[i] = sorted(graph[i], reverse=True)
# print("reverse graph = ", graph)
dfs(R)
# 3. 결과 출력
print("answer = ", answer)
for i in range(1, N+1):
    print(answer[i])