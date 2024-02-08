class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Get the length of the input list
        n = len(nums)
        
        # Initialize the result array with all 1s
        result = [1] * n
        
        # Variable to store the product of elements from left side
        left_product = 1
        
        # Compute the product of elements from left side and store in the result array
        for i in range(n):
            result[i] *= left_product
            left_product *= nums[i]
        
        # Variable to store the product of elements from right side
        right_product = 1
        
        # Compute the product of elements from right side and update the result array
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        # Return the final result array
        return result

        
