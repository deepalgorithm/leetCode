# divide = 42
# array = [0] * 1001
# answer = 0

# for _ in range(10):
#     n =  int(input())
#     moduler = n % divide
#     array[moduler] += 1

# for i in range(0, 1001):
#     if array[i] != 0:
#         answer += 1

# print(answer)

check = [0] * 42
answer = 0

for _ in range(10):
    n = int(input())
    moduler = n % 42
    check[moduler] += 1

for i in range(0, 42):
    if check[i] != 0:
        answer += 1

print(answer)