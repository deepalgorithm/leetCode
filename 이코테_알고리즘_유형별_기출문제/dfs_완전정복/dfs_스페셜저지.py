import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 함수
def dfs(idx):
    global visited, answer, graph, order

    visited[idx] = True
    answer[idx] = order
    order += 1

    for i in graph[idx]:
        if not visited[i]:
            dfs(i)


# 0. 입력 조건 
N = int(input())
visited = [False] * (N+1)
answer = [0] * (N+1)
order = 1
graph = [[] for _ in range(N+1)]

# 1. 그래프 받아오기
for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 2. dfs 수행
dfs(1)

# 3. 출력하기 
given = list(map(int, input().split()))
# answer.sort()
answer = answer[1:]
if given == answer:
    print(1)
else:
    print(0)