n = input()

result = []
value = 0

for x in n:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

result.append(str(value))

print(''.join(result))

