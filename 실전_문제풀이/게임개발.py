# N * M
n, m = map(int, input().split())
# 방문하지 않은 곳은 0 으로 표기
d = [[0] * m for _ in range(n)]
#x, y 좌표, d = 방향 [0,1,2,3] => [북,동,남,서]
x, y, direction = map(int, input().split())
# 현재 위치 방문처리
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]    

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재할 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다라면
        else:
            break
        turn_time = 0

print(count)