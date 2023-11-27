def containerWithMostWater(height):
    res = 0
    l = 0
    r = len(height) -1
    while l < r:
        area = min(height[l], height[r]) * (r -l)
        res = max(res, area)
        if height[l] < height[r]:
            l += 1
        elif height[r] < height[l]:
            r -= 1
        else:
            l += 1
    return res

print(containerWithMostWater([1,8,6,2,5,4,8,9,3,7]))