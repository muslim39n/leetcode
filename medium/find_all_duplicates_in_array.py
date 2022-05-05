class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        once = [False] * len(nums)

        i = 0

        while i < len(nums):
            if not once[nums[i] - 1]:
                once[nums[i] - 1] = True
                del nums[i]

            else:
                i += 1

        return nums

        
