class Solution:
    def arrayRankTransform(self, arr):
        n = sorted(arr)
        rank = {}
        r = 1

        for num in n:
            if num not in rank:
                rank[num] = r
                r += 1
        
        for i in range(len(arr)):
            arr[i] = rank[arr[i]]
        
        return arr