N, M = map(int, input().split())
A = list(map(int, input().split()))
l, r = 0, 0
answer = 0

while r < len(A):
    interval_sum = sum(A[l:r+1])
    if interval_sum == M:
        answer += 1
        l += 1
        r += 1
    elif interval_sum < M:
        r += 1
    else:
        l += 1

print(answer)