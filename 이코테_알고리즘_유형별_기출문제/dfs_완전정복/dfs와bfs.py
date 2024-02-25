# https://www.acmicpc.net/problem/1260

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dfs함수
def dfs(idx):
    global visited, graph
    visited[idx] = True
    print(idx, end=' ')

    for i in graph[idx]:
        if not visited[i]:
            dfs(i)

# bfs 함수
def bfs():
    queue = []
    queue.append(V)
    visited[V] = True

    while queue:
        idx = queue.pop(0)
        # print(idx)
        print(idx, end=' ')

        for i in graph[idx]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 0. 입력정보 설정

N,M,V = map(int, input().split())
visited = [False] * (N+1)
graph = [[] *(N+1) for _ in range(N+1)]

# 1. 그래프 정보 입력받기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
# 2. dfs
dfs(V)
print()

# 3. bfs 출력
visited = [False] * (N+1)
bfs()