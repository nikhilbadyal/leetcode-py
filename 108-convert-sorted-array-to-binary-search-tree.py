"""Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary
search tree.

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.



Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in a strictly increasing order.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def helper_node(self, nums: list[int], start: int, end: int) -> Optional["TreeNode"]:
        if start >= end:
            return None
        return TreeNode(
            nums[(start + end) // 2],
            self.helper_node(nums, start, ((start + end) // 2)),
            self.helper_node(nums, (1 + ((start + end) // 2)), end),
        )

    def sorted_array_to_bst(self, nums: list[int]) -> Optional["TreeNode"]:
        return self.helper_node(nums, 0, len(nums))


print(Solution().sorted_array_to_bst([-10, -3, 0, 5, 9]))
