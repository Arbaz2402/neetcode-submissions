class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1

        while k > 0:
            most_freq = max(count, key=count.get)
            ans.append(most_freq)
            count[most_freq] = 0
            k -= 1

        return ans