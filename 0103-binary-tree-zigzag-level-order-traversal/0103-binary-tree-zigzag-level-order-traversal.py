# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result =[]
        if root == None:
            return []
        q = deque([root])
        is_rev = False
        while len(q) != 0:
            level =[]
            size = len(q)
            for _ in range(size):
                curr = q.pop()
                level.append(curr.val)
                if curr.left:
                    q.appendleft(curr.left)
                if curr.right:
                    q.appendleft(curr.right)
                
            result.append(level[::-1] if is_rev else level)
            is_rev = not is_rev
        return result