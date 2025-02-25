class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for index in range(len(nums)-2, -1, -1):
            
            if nums[index] == nums[index+1]:
                if nums.count(nums[index]) > 2:
                    nums.remove(nums[index])
                    
            
                
        