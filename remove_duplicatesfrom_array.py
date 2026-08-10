class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nl = []
        for i in nums:
            if i not in nl:
                nl.append(i)
        for i in range(len(nl)):
            nums[i]=nl[i]
        return len(nl)