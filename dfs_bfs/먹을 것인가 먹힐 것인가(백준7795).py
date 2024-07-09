T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    main, sub = 0, 0
    count = 0

    while main < N:
        if sub == M:
            count += sub
            main += 1
        else:
            if A[main] > B[sub]:
                sub += 1
            else:
                count += sub
                main += 1
                
    print(count)
             