class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [''] * numRows

        i = 0
        j = 0
        jpp = True

        while i < len(s):
            rows[j] += s[i]

            i += 1

            if jpp:
                j += 1

                if j == numRows:
                    j -= 2
                    jpp = False

            else:
                j -= 1

                if j == -1:
                    j += 2
                    jpp = True

        ans = ''
        for i in rows:
            ans += i


        return ans

        
