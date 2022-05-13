class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans = ''

        for t in dictionary:
            if len(t) > len(s) or t[0] not in s:
                continue

            i = s.index(t[0]) + 1
            j = 1

            while j < len(t) and i < len(s) and i + len(t) - j <= len(s):
                if s[i] == t[j]:
                    j += 1

                i += 1

            if j == len(t) and (len(t) > len(ans) or len(t) == len(ans) and t < ans):
                ans = t

        return ans
