from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)

        for num in nums:

            # Skip duplicates
            if num - 1 in seen:
                continue

            curr = 1

            # Find consecutive numbers
            while num + 1 in seen:
                curr += 1
                num += 1

            longest = max(longest, curr)

        return longest