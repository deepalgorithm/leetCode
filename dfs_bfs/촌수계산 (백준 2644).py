import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx, count):
    global graph, visited, end, answer
    visited[idx] = True
    if idx == end:
        answer = count
        return

    for i in range(1, N+1):
        if not visited[i] and graph[idx][i]:
            dfs(i, count+1)

# 0. 입력 초기화
N = int(input())
start, end = map(int, input().split())
M = int(input())
MAX = 100 + 10
graph = [[False] * MAX for _ in range(MAX)] 
visited = [False] * MAX
answer = -1

# 1. 그래프에 연결 정보 채우기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True
# 2. DFS 호출

dfs(start, 0)

# 3. 출력

print(answer)