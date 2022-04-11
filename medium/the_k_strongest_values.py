class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()

        m = arr[(len(arr) - 1) // 2]

        i = 0
        j = len(arr) - 1

        ans = []

        while k > 0 and i <= j:
            if abs(arr[i] - m) > abs(arr[j] - m):
                ans.append(arr[i])
                i += 1

            else:
                ans.append(arr[j])
                j -= 1

            k -= 1

        return ans
