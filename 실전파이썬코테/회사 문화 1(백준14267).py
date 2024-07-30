import sys
input = sys.stdin.readline
sys.setrecursionlimit = 1000000

N,M = list(map(int, input().split()))
parent = list(map(int, input().split()))

for i in range(1, N):
    parent[i] -= 1

good = [0] * N
for _ in range(M):
    id, score = list(map(int, input().split()))
    good[id -1] += score

total_good = [0] * N

for i in range(1, N):
    total_good[i] = total_good[parent[i]] + good[i]

print(*total_good)