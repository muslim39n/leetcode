class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True

        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        handUn = [hand[0], ]
        cnt = [1, ]

        i = 1
        while i < len(hand):
            if handUn[-1] == hand[i]:
                cnt[-1] += 1

            else:
                handUn.append(hand[i])
                cnt.append(1)

            i += 1

        groups = len(hand) // groupSize

        while groups > 0:
            if len(handUn) < groupSize:
                return False

            i = 1
            cnt[0] -= 1

            while i < groupSize:
                if handUn[i] != handUn[i - 1] + 1:
                    return False

                cnt[i] -= 1
                i += 1

            i -= 1

            while i >= 0:
                if cnt[i] == 0:
                    del cnt[i]
                    del handUn[i]

                i -= 1

            groups -= 1

        return True




        
