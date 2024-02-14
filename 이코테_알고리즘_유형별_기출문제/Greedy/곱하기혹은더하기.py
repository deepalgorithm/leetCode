# 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S
# 문자열을 더하거나 곱해서 최대값 만들기

nums = input()

result = 0

for num in nums:
    num = int(num)
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)