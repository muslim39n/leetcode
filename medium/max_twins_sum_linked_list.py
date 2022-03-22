class Solution:
    def sumOfTwins(self, node, i):
        if node is None:
            return

        self.n += 1

        self.sumOfTwins(node.next, i + 1)

        if i >= self.n // 2:
            self.vals.append(node.val)

        else:
            sm = node.val + self.vals[i]

            if sm > self.mx:
                self.mx = sm

    def pairSum(self, head: Optional[ListNode]) -> int:
        self.n = 0
        self.vals = []
        self.mx = 0

        self.sumOfTwins(head, 0)

        return self.mx
