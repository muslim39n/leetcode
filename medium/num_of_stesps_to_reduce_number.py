def binPlusOne(s):
    i = len(s) - 1

    while i >= 0 and s[i] == '1':
        i -= 1

    if i < 0:
        return '1' + '0' * len(s)

    return s[:i] + '1' + '0' * (len(s) - i - 1)

class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0

        while s != '1':
            if s[-1] == '0':
                s = s[:-1]

            else:
                s = binPlusOne(s)

            steps += 1

        return steps
        
