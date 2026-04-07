# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False

        if root.val != subRoot.val:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            res = True
            d = deque([(root, subRoot)])
            while d:
                root, subRoot = d.popleft()
                print(root.val, subRoot.val)

                if root.left and subRoot.left:
                    if root.left.val != subRoot.left.val:
                        res = False
                        break
                    d.append((root.left, subRoot.left))
                elif root.left != subRoot.left:
                    res = False
                    break

                if root.right and subRoot.right:
                    if root.right.val != subRoot.right.val:
                        res = False
                        break
                    d.append((root.right, subRoot.right))
                elif root.right != subRoot.right:
                    res = False
                    break
                
            if res:
                return res
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)