class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i == 0 or flowerbed[i - 1] == 0:
                    if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        count += 1
                        i += 1
            i += 1
        return count >= n

