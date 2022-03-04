def isPalindrome(s):
    return s == s[::-1]

class Solution:
    def palindromes(self, ind, palArr):
        if ind == len(self.s):
            self.ans.append(palArr.copy())

        i = ind

        while i < len(self.s):
            if self.s[i] == self.s[ind] and isPalindrome(self.s[ind:i+1]):
                palArr.append(self.s[ind:i+1])
                self.palindromes(i + 1, palArr)
                del palArr[-1]

            i += 1


    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.ans = []

        self.palindromes(0, [])

        return self.ans
        
