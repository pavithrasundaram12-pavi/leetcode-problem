class Solution:
    def firstStableIndex(self, nums,k):
        n = len(nums)
        premax = [0] * n
        suffmin = [0] * n

        premax[0] = nums[0]
        suffmin[n - 1] = nums[n - 1]

        for i in range(1, n): premax[i] = max(premax[i - 1], nums[i])
        for i in range(n - 2, -1, -1): suffmin[i] = min(suffmin[i + 1], nums[i])
        for i in range(n):
            if premax[i] - suffmin[i] <= k: return i

        return -1