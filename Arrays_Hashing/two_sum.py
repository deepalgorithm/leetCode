from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_hash = {}
        for i, n in enumerate(nums):
            diff = target -n
            if diff in sum_hash:
                return [sum_hash[diff], i]
            sum_hash[n] = i
        return
    
s = Solution()

print(s.twoSum([2,7,11,15], 9))