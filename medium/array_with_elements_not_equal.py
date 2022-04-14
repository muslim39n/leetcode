class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        ans = []

        i, j = 0, len(nums) - 1


        while i < j:
            ans.append(nums[i])
            ans.append(nums[j])

            i += 1
            j -= 1

        if i == j:
            ans.append(nums[i])

        return ans
