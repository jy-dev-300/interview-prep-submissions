class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert to set
        # [2,20,4,10,3,4,5]
        # {5, 20, 4, 10, 3, 2}
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums = set(nums)
        # find all start of consecutive sequences
        lengths = []
        for num in nums:
            # is num right before this missing?
            if num -1 not in nums:
                # if yes this is start of seq so length = 1 to start
                length = 1
                # increment thru each sequence item, start w/ +1
                incrementor = 1
                # keep searching for the next +1 item in sequence
                while num + incrementor in nums:
                    incrementor += 1
                    length += 1
                lengths.append(length) 
        return max(lengths)