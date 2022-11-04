class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        p = 1
        # 왼쪽
        for num in nums:
            
            output.append(p)
            p *= num
        p = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= p
            p *= nums[i]
            
        return output