class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #k = num , v = count
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        tuples = sorted(d.items(), key=lambda item: item[1]) # sort by value via lambda fn
        # tuples = min to max [(num1, count1), (num2, count2), etc]

        output = []
        for tup in tuples[-k:]:
            output.append(tup[0])
        return output


        


















        