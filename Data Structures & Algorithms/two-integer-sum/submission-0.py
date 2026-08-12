class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        for i in range(len(nums)):
            # 1. Corrected math: target - current_number
            secondNumber = target - nums[i]
            
            # Create the sliced remaining array
            remaining_nums = nums[i+1:]
            
            # 2. Check if the number exists in the remaining part
            if secondNumber in remaining_nums:
                # 3. Find index in slice, then add offset (i + 1) to match original array
                secondIndex = remaining_nums.index(secondNumber) + (i + 1)
                return [i, secondIndex]
                
        return []