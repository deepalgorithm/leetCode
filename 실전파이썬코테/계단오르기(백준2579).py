N = int(input())

S = [0] * N

for i in range(N):
    S[i] = int(input())

A = [0] * N
B = [0] * N

A[0] = S[0]
B[0] = S[0]

for i in range(1, N):
    if i >= 2:
        A[i] = S[i] + max(A[i -2], B[i - 2])
    else:
        A[i] = S[i]
    
    if i >= 3:
        B[i] = S[i] + S[i -1] + max(A[i -3], B[i -3])
    else:
        B[i] = S[i] + S[i -1]

print(max(A[N-1], B[N-1]))