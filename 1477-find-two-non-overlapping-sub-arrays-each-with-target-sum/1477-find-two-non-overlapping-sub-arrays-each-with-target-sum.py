class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

      
        best = [float('inf')] * (n + 1)

        left = 0
        current_sum = 0
        answer = float('inf')

        for right in range(n):
            current_sum += arr[right]

           
            while current_sum > target:
                current_sum -= arr[left]
                left += 1

            if current_sum == target:
                length = right - left + 1

                
                if best[left] != float('inf'):
                    answer = min(answer, length + best[left])

                
                best[right + 1] = min(best[right], length)
            else:
                best[right + 1] = best[right]

        return -1 if answer == float('inf') else answer