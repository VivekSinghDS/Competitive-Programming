class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, ans = 0,0
        window = {}
        for r in range(len(nums)):
            window[nums[r]] = 1 + window.get(nums[r], 0)
            
            while(window.get(0, 0)>k):
                # print(nums[l:r+1])
                window[nums[l]]-=1
                l+=1
                
            ans = max(ans, r-l+1)
            
        return ans
        
