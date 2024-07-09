n = 28
students = [0] * 31
students[0] = 1

for _ in range(n):
    turned = int(input())
    students[turned] = 1

answer =[]

for i in range(1, 31):
    if students[i] == 0:
        answer.append(i)

for i in answer:
    print(i)