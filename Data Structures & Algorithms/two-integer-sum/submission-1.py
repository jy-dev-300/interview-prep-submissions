class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums has one pair i,j = target
        #return [i,j]
        #dictionary = things I've already seen     
        d = {}
        for j, num in enumerate(nums):
            diff = target - num
            if diff in d:
                i = d[diff]
                return [i,j]
            else:
                d[num] = j