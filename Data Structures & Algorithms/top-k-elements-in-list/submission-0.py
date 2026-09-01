class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # signature : group or count of group
        # num : count
        d = {}
        #store counts of each num/set of nums in dict
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        #sort dictionary by value descending, return top k
        #Bucket Sort는 값의 범위(range)를 여러 bucket으로 나누고, 각 값을 해당 bucket에 넣은 뒤 bucket 순서대로 처리하는 sorting 방식이야.

        buckets = [[] for _ in range(len(nums)+ 1) ]
        for num, count in d.items():
            buckets[count].append(num)

        ans = []
        for i in range(len(buckets) -1,0,-1):
            for num in buckets[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans

        