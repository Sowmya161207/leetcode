class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two indices such that nums[i] + nums[j] == target.

        Approach:
        - Check every possible pair of elements.
        - Return the indices when the target sum is found.

        Time Complexity: O(n²)
        Space Complexity: O(1)
        """

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]