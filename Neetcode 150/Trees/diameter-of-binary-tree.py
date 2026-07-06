# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # calculates height AND the diameter as height is being calculated
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0 
            
            left = dfs(root.left)
            right = dfs(root.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        
        height(root)
        return self.res

       
    

