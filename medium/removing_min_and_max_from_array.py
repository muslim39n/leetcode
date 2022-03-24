class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mx = mn = nums[0]
        mxi = mni = 0

        for i in range(1,len(nums)):
            if nums[i] > mx:
                mx, mxi = nums[i], i

            elif nums[i] < mn:
                mn, mni = nums[i], i

        if mxi < mni:
            mni, mxi = mxi, mni

        return min(mxi + 1, len(nums) - mni, mni + 1 + len(nums) - mxi)
                
