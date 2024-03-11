"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4



Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104
"""


class Solution(object):
    def search_insert(self, nums: list[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] >= target:
                return 0
            if nums[0] < target:
                return 1
        start_idx = 0
        end_idx = len(nums) - 1
        injection_point = 0
        while end_idx >= start_idx:
            mid = (end_idx + start_idx) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                start_idx = mid + 1
                injection_point = start_idx
            else:
                end_idx = mid - 1
                injection_point = mid + 1
        return injection_point


print(Solution().search_insert([1, 8, 9, 11, 13, 16, 19], 7))
