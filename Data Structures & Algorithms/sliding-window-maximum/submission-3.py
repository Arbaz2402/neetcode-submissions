class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ans = []
        q = []
        l = 0

        for r in range(len(nums)):

            # Remove smaller elements
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # Window is not complete yet
            if r - l + 1 < k:
                continue

            # Maximum
            ans.append(nums[q[0]])

            # Remove element leaving window
            if q[0] == l:
                q.pop(0)

            l += 1

        return ans