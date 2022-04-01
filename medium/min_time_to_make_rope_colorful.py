class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0

        curColor = colors[0]
        mxTime = neededTime[0]
        sm = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] != curColor:
                ans += sm - mxTime
                curColor = colors[i]
                mxTime = sm = neededTime[i]

            else:
                sm += neededTime[i]
                mxTime = max(mxTime, neededTime[i])

        ans += sm - mxTime

        return ans

        
