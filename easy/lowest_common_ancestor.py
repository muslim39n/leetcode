# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def ancestor(self, node):
        if node is None or self.ans is not None:
            return (False, False)

        pf = False
        qf = False

        if node == self.p:
            pf = True

        elif node == self.q:
            qf = True

        ans = self.ancestor(node.left)

        if ans[0] and ans[1]:
            return ans

        pf = pf or ans[0]
        qf = qf or ans[1]

        ans = self.ancestor(node.right)

        if ans[0] and ans[1]:
            return ans

        pf = pf or ans[0]
        qf = qf or ans[1]

        if pf and qf:
            self.ans = node

        return (pf, qf)





    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q

        self.ans = None

        self.ancestor(root)
        return self.ans
