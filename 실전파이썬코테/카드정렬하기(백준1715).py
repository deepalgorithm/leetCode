from queue import PriorityQueue

N = int(input())

pq = PriorityQueue()

for _ in range(N):
    num_cards = int(input())
    pq.put(num_cards)


answer = 0 
while pq.qsize() > 1:
    min_value1 = pq.get()
    min_value2 = pq.get()
    pq.put(min_value1 + min_value2)
    answer += min_value1 + min_value2

print(answer)