class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        pre = [0] * n
        minSum = float('inf')

        pre[0] = nums[0]

        for i in range(1, n):
            pre[i] = pre[i - 1] + nums[i]

        for win in range(l, r + 1):
            for j in range(win - 1, n):

                winSum = pre[j]

                if j - win >= 0:
                    winSum -= pre[j - win]

                if winSum > 0:
                    minSum = min(minSum, winSum)

        return -1 if minSum == float('inf') else minSum
        
        