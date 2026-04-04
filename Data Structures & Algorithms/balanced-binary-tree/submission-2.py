# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depth, is_balanced = self.depth(root)

        return is_balanced
    
    def depth(self, node: Optional[TreeNode]) -> (int, bool):
        if not node:
            return 0, True

        left_depth, left_is_balanced = self.depth(node.left)
        right_depth, right_is_balanced = self.depth(node.right)

        is_balanced = left_is_balanced and right_is_balanced and abs(left_depth - right_depth) <= 1

        return max(left_depth, right_depth) + 1, is_balanced


            