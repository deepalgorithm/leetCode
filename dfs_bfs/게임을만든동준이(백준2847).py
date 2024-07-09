N = int(input())
L = [0] * N

for i in range(N):
    L[i] = int(input())

count = 0
for i in range(N-2, -1, -1):
    if L[i] >= L[i + 1]:
        count += L[i] - (L[i+1] -1)
        L[i] = L[i+1] - 1
print(count)