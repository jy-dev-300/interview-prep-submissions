class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums has one pair i,j = target
        #return [i,j]
        #dictionary = things I've already seen     
        d ={}
        for j in range(len(nums)):
            diff = target - nums[j]
            if diff in d:
                i = d[diff]
                return [i,j]
            else:
                d[nums[j]] = j


