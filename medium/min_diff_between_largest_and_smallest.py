class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0

        mxs = [-10 ** 9 - 1] * 4
        mns = [10 ** 9 + 1] * 4

        for i in nums:
            if i > mxs[0]:
                mxs[0] = i

                if i > mxs[1]:
                    mxs[0], mxs[1] = mxs[1], mxs[0]

                    if i > mxs[2]:
                        mxs[1], mxs[2] = mxs[2], mxs[1]

                        if i > mxs[3]:
                            mxs[2], mxs[3] = mxs[3], mxs[2]


            if i < mns[0]:
                mns[0] = i

                if i < mns[1]:
                    mns[0], mns[1] = mns[1], mns[0]

                    if i < mns[2]:
                        mns[1], mns[2] = mns[2], mns[1]

                        if i < mns[3]:
                            mns[2], mns[3] = mns[3], mns[2]

        ans = min(mxs[3] - mns[0], mxs[2] - mns[1], mxs[1] - mns[2], mxs[0] - mns[3])

        #return max(ans, 0)
        return ans

        
