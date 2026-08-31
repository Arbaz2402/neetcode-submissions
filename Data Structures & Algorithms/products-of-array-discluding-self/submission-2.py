from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        left = [1] * n
        right = [1] * n
        ans = [1] * n

        # Fill left array
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # Fill right array
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # Multiply left and right
        for i in range(n):
            ans[i] = left[i] * right[i]

        return ans