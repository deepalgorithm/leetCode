# https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

#함수
def dfs(idx):
    global graph, visited
    visited[idx] = True
    
    for i in range(1, N+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)


# 0. 입력초기화
MAX = 1000 * 10
N, M = map(int, input().split())
graph = [[False] * MAX for _ in range(MAX)]
visited = [False] * MAX
answer = 0

# 1. graph에 연결 정보 채우기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True


# 2. dfs 호출
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        answer += 1

# 3. 출력
print(answer)