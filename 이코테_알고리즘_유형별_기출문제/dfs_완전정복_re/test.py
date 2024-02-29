from collections import deque

def solution(maps):
    queue = deque()
    max_y = len(maps)
    max_x = len(maps[0])
    
    visited = [[False] * max_y for _ in range(max_x)]
    dirY = [-1,1,0,0]
    dirX = [0,0,-1,1]
    
    visited[0][0] = True
    
    queue.append((0,0))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            newY = y + dirY[i]
            newX = x + dirX[i]
            
            if 0 <= newY < max_y and 0 <= newX < max_x and maps[newY][newX] == 1:
                if not visited[newY][newX]:
                    visited[newY][newX] = True
                    queue.append((newY,newX))
                    maps[newY][newX] = maps[y][x] + 1
    if maps[max_y - 1][max_x -1] == 1:
        return -1
    else:
        return maps[max_y-1][max_x-1]
        
print(solution(	[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))