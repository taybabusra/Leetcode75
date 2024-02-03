class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        s = list(s)
        v = ['a', 'e', 'i', 'o', 'u']

        while i < j:
            if s[i].lower() in v and s[j].lower() in v:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i].lower() in v and s[j].lower() not in v:
                j -= 1
            elif s[i].lower() not in v and s[j].lower() in v:
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(s)
