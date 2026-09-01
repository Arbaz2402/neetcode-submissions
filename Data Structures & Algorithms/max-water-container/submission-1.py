class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        ans = 0
        while l<r:
            width =  r - l
            height = min(heights[l], heights[r])
            area = width * height
            ans = max(ans,area)
            if heights[l]> heights[r]:
                r-=1
            else:
                l+=1
            
        return ans