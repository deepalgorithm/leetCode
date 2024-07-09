n = int(input())
input = input()
sum = 0

for i in range(n):
    sum += ord(input[i]) - ord('0')

print(sum)