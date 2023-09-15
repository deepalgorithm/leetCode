from collections import defaultdict
from typing import List

def groupAnagram(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list) #mapping charCount to List of Anagrams

    for s in strs:
        count = [0] * 26 # a ... z

        for c in s:
            count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)
    return res.values()



input = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagram(input))