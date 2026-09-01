#input : nums, output : boolean true if a num appears more than once
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        length_of_array = len(nums)
        size_of_set = len(set(nums))
        if length_of_array > size_of_set:
            return True
        else:
            return False


        