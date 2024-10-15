import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
visited = [False] * N
parent = [-1] * N

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a -1].append(b - 1)
    graph[b -1].append(a - 1)

def dfs(index):
    visited[index] = True

    for i in graph[index]:
        if not visited[i]:
            parent[i] = index + 1
            dfs(i)

dfs(0)

for i in range(1, len(parent)):
    print(parent[i])
