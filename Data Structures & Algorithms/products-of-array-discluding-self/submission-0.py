class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #create array with [1] for every number
        res = [1] * len(nums)

        #Initially prefix 1 because 1 if out of bounds
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res