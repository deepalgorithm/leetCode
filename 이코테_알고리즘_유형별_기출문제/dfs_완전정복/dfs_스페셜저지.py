import sys

N = int(sys.stdin.readline())
graph=[[] for _ in range(N+1)]

for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

ans= list(map(int,sys.stdin.readline().split()))

level=[False]*(N+1)
tsize = [0]*(N+1)
visited = [False]*(N+1)

def dfs(x,lv):
    if visited[x]:
        return 0
    visited[x]=True
    size=1
    level[x]=lv
    for i in range(len(graph[x])):
        next =graph[x][i]
        size+=dfs(next,lv+1)
    tsize[x]=size
    return size


if ans[0]!=1:
    print("0")
    sys.exit(0)
else:
    dfs(1,0)
    for i in range(1,N):
        x=ans[i]
        if tsize[x] == 1 or i + tsize[x] >=N:
            continue
        next = ans[i+tsize[x]]
        if level[next]>level[x]:
            print(0)
            sys.exit(0)
    print(1)
'''안녕하세요! 해당 문제는 DFS를 정확히 이해해야 되기도 했지만, 
한 노드를 기준으로 갈 수 있는 자식 노드들을 순서와 관계없이 구분할 방법도 필요했습니다. 
그래서 무조건 정답이 뭔지를 찾거나,
작성하신 대로 모든 경우의 수를 다 따지면 시간 초과가 발생할 것 같아요!

그래서 필요한 것은 각 노드를 루트로 하는 서브트리의 크기를 게산하고,
각 노드의 높이(레벨)를 계산해야 됐습니다. 그래서 문제에서 주어진 정답이
순서와 관계 없이 정답이 될 수 있는지 서브트리 수준에서 판단이 필요했던 것으로 보입니다!

샘플 정답은 이걸 참고하시면 될 것 같습니다!'''