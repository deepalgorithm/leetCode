def gpt_sort_key(num):
    if '.' in num:
        x, y = map(int, num.split('.'))
    else:
        x, y = int(num), -1  # 정수는 소수점 부분을 -1로 처리
    return (x, y)


N = int(input())
numbers = [input().strip() for _ in range(N)]

sorted_numbers = sorted(numbers, key=gpt_sort_key)

for num in sorted_numbers:
    print(num)
