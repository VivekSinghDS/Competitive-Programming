class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        new_threshold = threshold*k
        
        l, ans, sumr = 0,0,0
        
        for r in range(len(arr)):
            sumr += arr[r]
            
            if(r - l + 1 == k):
                if(sumr >= new_threshold):
                    ans+=1
                    
                sumr-=arr[l]
                l+=1
                
        return ans
            
        
