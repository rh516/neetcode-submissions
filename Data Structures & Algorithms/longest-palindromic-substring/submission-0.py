class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        longestSize = 0

        def expand(s, left, right):
            nonlocal longest, longestSize

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longestSize:
                    longest = s[left : right + 1]
                    longestSize = right - left + 1
                    
                left -= 1
                right += 1

        for i in range(len(s)):
            expand(s, i, i)
            expand(s, i, i + 1)

        return longest