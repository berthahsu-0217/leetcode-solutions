class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #pointers pointing different colors
        red, white, blue = 0, 0, len(nums)-1
        
        while white <= blue:
            if nums[white] == 0: #pointing to red, swap elements with red pointer
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1: #pointing to white, increment white pointers
                white += 1
            else: #pointing to blue, swap elements with blue pointer
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
        return
                
        
        
        