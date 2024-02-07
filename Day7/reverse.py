class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string `s` into words using the split() method
        # Reverse the order of the words using the reversed() function
        # Join the reversed words into a single string separated by a space using the join() method
        return " ".join(reversed(s.split()))

