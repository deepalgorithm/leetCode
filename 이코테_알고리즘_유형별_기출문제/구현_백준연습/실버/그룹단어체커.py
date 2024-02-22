N = int(input())
cnt = N

for i in range(N):
    words = input()
    for j in range(0, len(words)-1):
        if words[j] == words[j+1]:
            pass
        elif words[j] in words[j+1:]:
            cnt -= 1
            break

print(cnt)