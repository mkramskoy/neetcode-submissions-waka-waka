# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_path = 0

        d = deque([root])
        while d:
            node = d.popleft()
            max_path = max(max_path, self.max_depth(node.left) + self.max_depth(node.right))
            if node.left:
                d.append(node.left)
            if node.right:
                d.append(node.right)

        return max_path

    def max_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = 0
        if root.left:
            left_depth = self.max_depth(root.left)
            print(f"left {left_depth}")

        right_depth = 0
        if root.right:
            right_depth = self.max_depth(root.right)
            print(f"right {right_depth}")

        return 1 + max(left_depth, right_depth)