n, array = int(input()), list(map(int, input().split()))

result = [array[0]]

for i in range(1, n):
    #print(array[i] * (i +1), sum(result))
    result.append(array[i] * (i+1) - sum(result))

#print(result)
    
for i in result:
    print(i, end=" ")