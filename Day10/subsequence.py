class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        positions = {}
        for i, char in enumerate(t):
            if char not in positions:
                positions[char] = []
            positions[char].append(i)
        
        prev_pos = -1
        for char in s:
            if char not in positions:
                return False
            pos_list = positions[char]
            left = 0
            right = len(pos_list) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if pos_list[mid] > prev_pos:
                    right = mid - 1
                else:
                    left = mid + 1
            if left == len(pos_list):
                return False
            prev_pos = pos_list[left]
        return True
