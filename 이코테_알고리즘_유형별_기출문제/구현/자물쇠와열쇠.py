key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

def zip_rotate(original):
    rotated = list(zip(*original[::-1]))
    return rotated

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False  
    return True

# rotated = zip_rotate(key)
# print(key)
# print(rotated)
# print("--------------------------------")
# rotated = zip_rotate(rotated)s
# print(rotated)

def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0] * (n*3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for _ in range(4):
        key = zip_rotate(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]

                if check(new_lock) == True:
                    return True
                
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    return False

print(solution(key, lock))