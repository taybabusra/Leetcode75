
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies among all kids
        max_candies = max(candies)
        
        # Initialize an empty list to store the result
        result = []
        
        # Iterate through the list of candies
        for candy_count in candies:
            # Check if giving the extra candies to the current kid
            # would make them have the greatest number of candies
            if candy_count + extraCandies >= max_candies:
                # If so, append True to the result list
                result.append(True)
            else:
                # If not, append False to the result list
                result.append(False)
        
        # Return the result list
        return result
