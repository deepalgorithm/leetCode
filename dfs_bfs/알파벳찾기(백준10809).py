input = input()
answer = [-1] * 26

for i in range(0, len(input)):
    index = ord(input[i]) - ord('a')
    if answer[index] == -1:
        answer[index] = i

for i in answer:
    print(i, end=' ')