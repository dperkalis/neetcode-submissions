class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)-1
        
        s_lower = "".join(c for c in s if c.isalnum()).lower()
        l = len(s_lower)
        
        if l == 1 or l == 0:
            return True

        for i, j in zip(range(l-1), range(l-1,0,-1)):
            if s_lower[i] != s_lower[j]:
                return False

        return True