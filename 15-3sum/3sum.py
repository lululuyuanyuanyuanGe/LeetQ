class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n= len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    result.append([nums[i], nums[right], nums[left]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[left] == nums[right - 1]:
                        right -= 1
                    
                    right -= 1
                    left += 1
                
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        return result
