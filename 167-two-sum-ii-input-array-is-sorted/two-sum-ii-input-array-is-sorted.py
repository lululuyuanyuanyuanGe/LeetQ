class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        indexes = []
        for i in range(1, len(numbers)):
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -=1
        return []