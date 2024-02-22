import sys

n,m = map(int, sys.stdin.readline().rstrip().split())

data = [] # 초기 맵 리스트

temp = [[0] * m for _ in range(n)]  # 벽을 설치한 뒤의 맵 리스트

# 지도 모양 입력받기
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

# 북, 동, 남, 서 4가지 방향 이동
dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

#바이러스 유출
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상 하 좌 우 바이러스가 퍼질 수 있는 경우
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                #해당 위치에 바이러스 배치 후, 재귀
                temp[nx][ny] = 2
                virus(nx, ny)
    return

#현재 맵에서 안전 영역의 크기를 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 벽을 설치하면서 매번 안전 거리 계산

def dfs(count):
    global result
    # 벽이 총 3개인 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
    # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                #현 위치에 바이러스가 있다면 바이러스 확산
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전영역의 최대값 계산
        result = max(result, get_score())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                # dfs 함수 재귀적으로 수행
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)

print(result)