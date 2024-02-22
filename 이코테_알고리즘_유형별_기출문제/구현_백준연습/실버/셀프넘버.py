## https://www.acmicpc.net/problem/4673


SET = [i for i in range(1,10001)]

def self_num(n):
    number = n
    n = str(n)
    for i in n:
        number += int(i)
    return number


for n in range(1, 100001):
    if self_num(n) in SET:
        SET.remove(self_num(n))

for i in range(len(SET)):
    print(SET[i])