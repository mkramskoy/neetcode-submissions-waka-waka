# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: if root is None, or root matches either p or q
          if not root or root.val == p.val or root.val == q.val:
              return root

          # Recursively search left and right subtrees
          left = self.lowestCommonAncestor(root.left, p, q)
          right = self.lowestCommonAncestor(root.right, p, q)

          # If both left and right return nodes, root is the LCA
          if left and right:
              return root

          # If only one side has a result, return that side
          # (handles case where p and q are on same side)
          return left if left else right