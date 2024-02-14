#Q1 _ 모험가 길드

#입력 : 첫째줄 - 모험가의 수 N, 둘째줄 - 모험가의 공포도 값의 리스트
#출력 : 여행을 떠날 수 있는 그룹 수의 최댓값 출력

N = int(input())

lst = list(map(int, input().split()))

# 오름차순으로 정렬
lst.sort() 
#총 그룹의 수
result = 0
#현재 그룹에 포함되어 있는 모험가 수 카운트
count = 0

for i in lst:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)
