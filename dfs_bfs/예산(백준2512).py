import sys
input = sys.stdin.readline

N = int(input())
budget = list(map(int, input().split()))
M = int(input())

left = 0
right = max(budget)
answer = -1

while left <= right:
    middle = (left + right) // 2

    sum = 0
    for i in range(N):
        sum += min(middle, budget[i])

    if sum <= M:
        answer = middle
        left = middle + 1
    else:
        right = middle -1

print(answer)