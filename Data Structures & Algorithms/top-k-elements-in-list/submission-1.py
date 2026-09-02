class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # signature : group or count of group
        # num : count
        d = {}
        for i in range(len(nums)):
            curr = nums[i] 
            if (curr in d):
                d[curr] += 1
            else:
                d[curr] = 1
        #store counts of each num/set of nums in dict
        
        #Bucket Sort는 값의 범위(range)를 여러 bucket으로 나누고, 각 값을 해당 bucket에 넣은 뒤 bucket 순서대로 처리하는 sorting 방식이야.
        buckets = [[] for _ in range(len(nums) + 1)]
        res = []
        for num, count in d.items():
            buckets[count].append(num)

        for bucket in reversed(buckets):
            for item in bucket:
                res.append(item)
                if len(res) == k: 
                #Should this condition be evaluated 
                #before the change or after the change?”
                    return res

















# for i in range(len(buckets) - 1, -1, -1):
        