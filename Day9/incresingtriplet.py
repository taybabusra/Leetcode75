class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Check if the length of the array is less than 3
        if len(nums) < 3:
            return False
        
        # Initialize two variables to store the smallest and second smallest elements
        left , mid = float("inf"), float("inf")
        
        # Iterate through each element in the array
        for i in range(len(nums)):
            # Check if the current element is greater than the second smallest element
            if nums[i] > mid:
                return True  # If it is, we've found an increasing triplet subsequence
            
            # If the current element is smaller than the smallest element seen so far,
            # update the smallest element
            if nums[i] < left:
                left = nums[i]
            
            # If the current element is greater than the smallest element but smaller than
            # the second smallest element, update the second smallest element
            elif nums[i] > left and nums[i] < mid:
                mid = nums[i]
        
        # If no increasing triplet subsequence is found, return False
        return False
