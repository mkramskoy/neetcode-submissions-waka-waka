# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        d = deque([(root, 1)])
        res = 1

        while d:
            node, level = d.popleft()
            if node.left:
                d.append((node.left, level + 1))

            if node.right:
                d.append((node.right, level + 1))
            
            if level > res:
                res = level

        return res
        