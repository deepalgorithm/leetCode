import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

# 해쉬 값을 계산 하기 위한 준비물
mod = 1e9 + 7
po = [0] * M
po[0] = 1
for i in range(1, M):
    po[i] = po[i-1] * 31 % mod

#Pn
Pn = "I"
for i in range(N):
    Pn += "OI"

K = len(Pn)

#Pn의 해쉬 값 계산
Pn_hash = 0 
for i in range(K):
    Pn_hash *= 31
    Pn_hash %= mod

    Pn_hash += ord(Pn[i]) - ord('A') + 1
    Pn_hash %= mod

#S[0:len(Pn)]
S_hash = 0
for i in range(K):
    S_hash *= 31
    S_hash %= mod

    S_hash += ord(S[i]) - ord('A') + 1
    S_hash %= mod

#S의 부분 문자열들의 해쉬 값을 계산
count = 0
for i in range(0, M - K + 1):
    if S_hash == Pn_hash:
        count += 1

    # S_hash 갱신
    largest = ord(S[i]) - ord('A') + 1
    S_hash += mod - largest * po[K-1] % mod
    S_hash %= mod

    S_hash *= 31
    S_hash %= mod

    if i + K < M:
        S_hash += ord(S[i + K]) - ord('A') + 1
        S_hash %= mod

print(count)