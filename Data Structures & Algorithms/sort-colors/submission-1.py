class Solution:
    

    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        H=n-1
        L=0
        M=0

        while M<=H:
            if nums[M]==0:
                nums[L],nums[M]=nums[M],nums[L]
                L+=1
                M+=1
            elif nums[M]==1:
                M+=1
            else:
                nums[M],nums[H]=nums[H],nums[M]
                H-=1                
                


      
    