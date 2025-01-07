class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums_len = len(nums)
        k=k%nums_len
        rotate_part = nums[nums_len-k :]
        unaffect_part = nums[:nums_len-k]
        nums[:] = rotate_part + unaffect_part
        