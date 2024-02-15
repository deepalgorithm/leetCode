n = int(input())

data = list(map(int, input().split()))
target = 1
data.sort()

for i in data:
    if target < i:
        break
    target += i
print(target)
    
        
    