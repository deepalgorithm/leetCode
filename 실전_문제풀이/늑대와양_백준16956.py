R, C = map(int, input().split())

M = [list(input()) for i in range(R)]

# 동, 북, 서, 남
# dx = 세로, dy = 가로
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]

ck = False

for i in range(R):
    for j in range(C):
        if M[i][j] == 'w':
            for w in range(4):
                ii, jj = i + dx[w], j + dy[w]
                if ii < 0 or ii == R or jj < 0 or jj == C:
                    continue
                if M[ii][jj] == 'S':
                    ck = True

if ck :
    print(0)
else: 
    print(1)
    for i in range(R):
        for j in range(R):
            if M[i][j] not in 'SW':
                M[i][j] = 'D'
for i in M:
    print(''.join(i))