import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#함수 구현
def dfs(idx):
    global visited, answer, graph
    visited[idx] = True

    for i in graph[idx]:
        if not visited[i]:
            answer[i] = idx
            dfs(i)


# 0. 입력정보 받기
N = int(input())
visited = [False] * (N+1)
answer = [0] * (N+1)
graph = [[] for _ in range(N+1)]

# 1. 그래프 정보 입력
for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 2. dfs
    
dfs(1)

# 3. 정답출력

for i in range(2,N+1):
    print(answer[i])