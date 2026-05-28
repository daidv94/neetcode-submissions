class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = max_k = 0
        
        for num in nums:
            if num == 0:
                max_k = max(k, max_k)
                k = 0
            else:
                k = k + 1
        
        return max(k, max_k)