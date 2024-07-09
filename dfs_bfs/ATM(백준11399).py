N = int(input())
P = list(map(int, input().split()))
P.sort()
current_sum = 0

for i in range(N):
    current_sum = current_sum + P[i]
    P[i] = current_sum
print(sum(P))