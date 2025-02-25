class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        newArr = []
        max_count = 0
        repeated_elem = None

        for element in nums:
            if element not in newArr:
                newArr.append(element)
            
                count = nums.count(element)
                
                if count > max_count:
                    max_count = count
                    repeated_elem = element
        return repeated_elem
                    
        