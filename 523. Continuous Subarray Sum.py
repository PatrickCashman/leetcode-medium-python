class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        # Initialize with remainder 0 at index -1
        h_map = {0: -1}  
        total = 0

        for i, num in enumerate(nums):
            total += num
            remainder = total % k
            
            if remainder in h_map:
                # Ensure subarray length is at least 2
                if i - h_map[remainder] > 1:
                    return True
            else:
                h_map[remainder] = i

        return False

#time: O(n)

nums = [23,2,4,6,7]
k = 6
solution_instance = Solution()
print(solution_instance.checkSubarraySum(nums, k))