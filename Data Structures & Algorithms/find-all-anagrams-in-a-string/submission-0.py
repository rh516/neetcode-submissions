class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCount = {}
        for ch in p:
            pCount[ch] = pCount.get(ch, 0) + 1

        ans = []
        currentWindow = {}

        left = 0

        for right in range(len(s)):
            currentWindow[s[right]] = currentWindow.get(s[right], 0) + 1
            currentWindowSize = right - left + 1

            if currentWindowSize > len(p):
                currentWindow[s[left]] -= 1

                if currentWindow[s[left]] == 0:
                    del currentWindow[s[left]]

                left += 1

            if currentWindow == pCount:
                ans.append(left)

        return ans
