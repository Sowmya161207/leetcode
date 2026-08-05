class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            word=""
            for j in range(i,len(s)):
                if s[j] in word:
                    break
                word+=s[j]
            if len(word)>count:
                count=len(word)
        return count