from typing import List

def replaceElements(arr: List[int]) -> List[int]:
    #initial max = -1
    #reverse iteration
    #new max = max(oldmax, arr[i])

    rightMax = -1

    for i in range(len(arr)-1 , -1 ,-1):
        newMax = max(rightMax, arr[i])
        arr[i] = rightMax
        rightMax = newMax
    return arr
    
input = [17,18,5,4,6,1]


print(replaceElements(input))