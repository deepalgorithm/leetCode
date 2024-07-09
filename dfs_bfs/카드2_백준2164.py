import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
card = deque(list(range(1, N+1)))
drop = True

while len(card) > 1:
    if drop:
        card.popleft()
        drop = False
    else:
        x = card.popleft()
        card.append(x)
        drop = True

print(card[0])