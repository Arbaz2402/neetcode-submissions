class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        l = 0
        for r in range(1,len(nums)):
            while r-l<=k and r<len(nums):
                if nums[l] == nums[r]:
                    return True
                else:
                    r+=1
            l+=1
        return False