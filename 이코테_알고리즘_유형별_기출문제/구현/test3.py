# from itertools import combinations

# def is_prime(num):
#     return False if num == 1 or any(
#         [num % i ==0 for i in range(2, int(num**(1/2)+1))]) else True

# arr = [3,1,6,4,9]
# answer = 0

# for items in combinations(arr, 3):
#     print(items)
#     num = sum(items)
#     print(num)
#     if is_prime(num) == True:
#         answer += 1

# print(answer)

# def is_prime2(num):
#     return False if num ==1 or any(
#         [num % i == 0 for i in range(2, int(num**(1/2)+ 1))]) else True

# from collections import defaultdict

# def solution(participant, completion):
#     completion_status = defaultdict(int)

#     # Initialize completion status for each participant
#     for name in participant:
#         completion_status[name] += 1

#     # Update completion status based on the provided completions
#     for name in completion:
#         if name in completion_status:
#             completion_status[name] -= 1

#     # Find participants who did not complete the race
#     incomplete_participants = [name for name, completed in completion_status.items() if completed != 0]

#     return incomplete_participants

# print(solution(["marina", "josipa", "nikola", "vinko", "filipa","abc","ddf", "marina", "marina"]
# , ["josipa", "filipa", "marina", "nikola"]))
# prime_set = set()

# def isPrime(number):
#     # 6. 0과 1은 False
#     if number in (0, 1):
#         return False

#     # 7. 에라토스테네스의 체
#     lim = int(number ** 0.5 + 1)
#     for i in range(2, lim):
#         if number % i == 0:
#             return False

#     return True
    
# def makeCombinations(combination, others):
#     # 5. 탈출 조건 / 비교 조건 : 지금까지 만들어진 조합을 
#     if combination != "":
#         if isPrime(int(combination)):
#             prime_set.add(int(combination))
    
#     # 4. 현재까지 만들어진 숫자에, 남아있는 숫자 중 하나를 붙여서 조합을 만든다
#     for i in range(len(others)):
#         print("others[i] = "+others[i])
#         print("others[:i] = " + others[:i])
#         print(type(others[i]))
#         print("others[i+1:] = " + others[i+1:])
#         x = combination + others[i], others[:i] + others[i + 1:]
#         print(type(x))
#         print("combination + others[i], others[:i] + others[i + 1:] = "+ combination + others[i], others[:i] + others[i + 1:])

#         makeCombinations(combination + others[i], others[:i] + others[i + 1:])


# def solution(numbers):
#     # 2. 모든 조합을 만드는 recursive 함수를 수행한다.
#     makeCombinations("", numbers)

#     # 3. primeSet의 length를 반환해준다.
#     answer = len(prime_set)
#     return answer

# print(solution("17"))


def solution(progresses, speeds):
    answer = []
    
    while progresses:
        count = 0
        while progresses and progresses[0] >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
            
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]

        if count:
            answer.append(count)
        
    return answer

print(solution([93, 30, 55], [1, 30, 5]))