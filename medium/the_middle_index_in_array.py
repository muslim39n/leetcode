class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        smRight = sum(nums)
        smLeft = 0
        ind = 0

        while ind < len(nums):
            if smRight - nums[ind] == smLeft:
                return ind

            smRight -= nums[ind]
            smLeft += nums[ind]

            ind += 1

        return -1
        
