# https://www.acmicpc.net/problem/1743

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

print(graph)

