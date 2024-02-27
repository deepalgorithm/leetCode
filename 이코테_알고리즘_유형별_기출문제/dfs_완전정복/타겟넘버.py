def dfs(numbers, target, cur_idx, cur_sum):

    # 끝까지 다 간 경우
    if len(numbers) == cur_idx:
        if cur_sum == target:
            return 1
        else:
            return 0
    else:
        answer = 0
        answer += dfs(numbers, target, cur_idx + 1, cur_sum + numbers[cur_idx])
        answer += dfs(numbers, target, cur_idx + 1, cur_sum - numbers[cur_idx])
        return answer
 
def solution(numbers, target) : 
 	
    answer = dfs(numbers, target, 0, 0)
    return answer

print(solution([1,1,1,1,1], 3))