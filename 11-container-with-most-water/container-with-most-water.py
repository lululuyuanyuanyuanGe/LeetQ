class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            temp_area = 0
            if height[left] < height[right]:
                temp_area = (right - left) * height[left]
                if temp_area > area:
                    area = temp_area
                left += 1
            
            else:
                temp_area = (right - left) * height[right]
                if temp_area > area:
                    area = temp_area
                right -= 1
        return area