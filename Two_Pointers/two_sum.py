def two_sum(arr, target):
    l, r = 0, len(arr) -1
    while arr[l] + arr[r] != target:
        if arr[l] + arr[r] < target:
            l += 1
        else:
            r -= 1
    return [l+1, r+1]

print(two_sum([1,3,4,5,7,10,11], 9))