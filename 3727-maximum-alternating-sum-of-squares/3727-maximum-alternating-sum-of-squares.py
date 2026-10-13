class Solution(object):
    def maxAlternatingSum(self, a):
        n = len(a)
        sum = 0
        i, j = 0, n - 1

        for k in range(n):
            a[k] = a[k] * a[k]

        a.sort()
        ans = []

        while i < j:
            ans.append(a[j])
            ans.append(a[i])
            j -= 1
            i += 1

        if n & 1:
            ans.append(a[n // 2])

        for k in range(n):
            if k % 2 == 0:
                sum += ans[k]
            else:
                sum -= ans[k]

        return sum