class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        # Initialize a count to keep track of the number of flowers placed
        count = 0
        # Initialize the index to iterate through the flowerbed
        i = 0
        # Iterate through the flowerbed array
        while i < len(flowerbed):
            # Check if the current plot is empty
            if flowerbed[i] == 0:
                # Check if it's the first plot or if the previous plot is also empty
                if i == 0 or flowerbed[i - 1] == 0:
                    # Check if it's the last plot or if the next plot is also empty
                    if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                        # If all conditions are met, place a flower
                        flowerbed[i] = 1
                        # Increment the count of placed flowers
                        count += 1
                        # Move to the next plot
                        i += 1
            # Move to the next plot
            i += 1
        # Check if enough flowers have been placed
        return count >= n


