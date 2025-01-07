class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums_len = len(nums)    
        k=k%nums_len
        rotate_list = nums[nums_len-k:]
        new_list = nums[:nums_len-k]
        for i in range(len(new_list)):
            rotate_list.append(new_list[i])
        nums[:] = rotate_list
        