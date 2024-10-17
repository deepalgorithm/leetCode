N = int(input())

#점화식
a = [0] * (N +1) # 길이 N + 1, a[N]

a[1] = 0

for i in range(2, N +1):
    a[i] = 1 + a[i -1]

    if i % 3 == 0:
        a[i] = min(a[i], 1 + a[i // 3])
    if i % 2 == 0:
        a[i] = min(a[i], 1 + a[i // 2])

print(a[N])