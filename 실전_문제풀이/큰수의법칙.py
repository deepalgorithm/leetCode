N, M, K = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort()
first = num_list[-1]
second = num_list[-2]

result = 0

while True:
    for _ in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1

print(result)