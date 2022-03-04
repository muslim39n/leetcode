class Solution:
    def arrangements(self, i):
        if i == 0:
            self.ans += 1
            return
            
        for j in range(1, self.n + 1):
            if not self.used[j] and (i % j == 0 or j % i == 0):
                self.used[j] = True
                self.arrangements(i - 1)
                self.used[j] = False
        
    
    def countArrangement(self, n: int) -> int:
        self.used = [False] * (n + 1)
        self.ans = 0
        self.n = n
        
        self.arrangements(n)
        
        return self.ans