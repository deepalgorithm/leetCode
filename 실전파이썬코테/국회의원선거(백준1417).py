from queue import PriorityQueue

N = int(input())
check = [0] * N

for i in range(N):
    check[i] = int(input())

# print(max(check[1:len(check) + 1]))
pq = PriorityQueue()

for i in range(1, N):
    pq.put(-check[i])

if N == 1:
    print(0)
else:
    count = 0
    while True:
        max_value = -pq.get()
        if max_value < check[0]:
            break

        max_value -= 1
        check[0] += 1
        count += 1
        pq.put(-max_value)
    print(count)