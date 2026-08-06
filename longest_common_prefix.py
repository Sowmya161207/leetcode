class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        m = min(len(word) for word in strs)
        for i in range(m):
            ch = strs[0][i]
            for word in strs:
                if word[i] != ch:
                    return s
            s += ch
        return s