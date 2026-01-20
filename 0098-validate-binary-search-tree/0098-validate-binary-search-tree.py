# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result =[]
        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)

        if len(set(result)) != len(result):
            return False
        
        if result == sorted(result):
            return True
        else:
            return False
        
        return result

        
        
        