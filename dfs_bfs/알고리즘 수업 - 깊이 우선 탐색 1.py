import sys
sys.setrecursionlimit(10**6)
input =sys.stdin.readline

def dfs(idx):
    global graph, visited, answer, order
    visited[idx] = True
    answer[idx] = order
    order +=1

    for i in graph[idx]:
        if not visited[i]:
            dfs(i)

# 0. 입력조건
N, M, R = map(int, input().split())
MAX = 1000_000 + 10
graph = [[] for _ in range(N+1)]
visited = [False] * MAX
answer = [0] * MAX
order = 1
# 1. 그래프 입력
for _ in range(M):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 2. dfs 
for i in range(1, N +1):
    graph[i] = sorted(graph[i])

dfs(R)

# 3. 결과 출력
for i in range(1, N+1):
    print(answer[i])
