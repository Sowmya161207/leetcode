class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))

        if len(nums) < 3:
            return max(nums)

        for i in range(2):
            m = max(nums)
            nums.remove(m)
