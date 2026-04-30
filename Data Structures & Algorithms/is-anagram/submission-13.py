class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        length = len(s)
        counts = {}
        for i in range(length):
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1
       
        for i in range(length):
            if t[i] in counts:
                counts[t[i]] -=  1
      
        result = [v for v in counts.values() if v != 0]
        return len(result) == 0

                
            
                
            
            
        
        