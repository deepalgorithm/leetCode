n = input()

mid = len(n) // 2

left = sum([int(i) for i in n[:mid]])
right = sum([int(i) for i in n[mid:]])

if left == right:
    print('LUCKY')
else:
    print('READY')