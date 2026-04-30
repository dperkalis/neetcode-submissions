class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        counts = {}
        for i in range(len(s)):
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1
        print(counts)
        for i in range(len(t)):
            if t[i] in counts:
                counts[t[i]] -=  1
      
        result = [v for v in counts.values() if v != 0]
        return len(result) == 0

                
            
                
            
            
        
        