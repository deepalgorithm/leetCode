N,K,B = map(int, input().split())

check = [0] * N

for _ in range(B):
    broken = int(input())
    check[broken-1] = 1

psum = [0] * N
psum[0] = check[0]

for i in range(1, N):
    psum[i] = psum[i-1] + check[i]

check_sum = []

for i in range(0, N -K + 1):
    # i ~ i + K -1
    if i ==0:
        sum = psum[i + K -1]
    else:
        sum = psum[i + K -1] - psum[i - 1]
    check_sum.append(sum)

print(min(check_sum))