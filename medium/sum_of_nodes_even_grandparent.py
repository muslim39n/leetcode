
class Solution:
    def grandParents(self, node, isParentEven):



        if node.left:
            self.sum += isParentEven * node.left.val

            self.grandParents(node.left, node.val % 2 == 0)

        if node.right:
            self.sum += isParentEven * node.right.val

            self.grandParents(node.right, node.val % 2 == 0)

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum = 0

        self.grandParents(root, False)

        return self.sum
