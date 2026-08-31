from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        n = len(nums)
        ans = []

        for i in range(n):

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            rem = nums[i]

            l = i + 1
            r = n - 1

            while l < r:

                total = rem + nums[l] + nums[r]

                if total == 0:

                    ans.append([rem, nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # Skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicate right values
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif total < 0:
                    l += 1

                else:
                    r -= 1

        return ans