class Solution(object):
    def minimizeSum(self, nums):
        nums.sort()
        n=len(nums)
        a=nums[n-1]-nums[2]
        b=nums[n-2]-nums[1]
        c=nums[n-3]-nums[0]
        return min(a,b,c)       