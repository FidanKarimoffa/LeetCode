class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for numbers in range(len(nums)-2, -1, -1):
            if nums[numbers] == nums[numbers+1]:
                nums.pop(numbers)
        
            
        