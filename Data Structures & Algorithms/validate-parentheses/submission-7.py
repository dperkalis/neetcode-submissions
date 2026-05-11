class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
      
        i = 0
        
        while i < len(s):
            l = len(stack)
            if l == 0 and s[i] != '(' and s[i] != '{' and s[i] != '[':
                return False

            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')' and l > 0:
                curr = stack.pop()
                if curr != '(':
                    return False
            elif s[i] == '}' and l > 0:
                curr = stack.pop()
                if curr != '{':
                    return False
            elif s[i] == ']' and l > 0:
                curr = stack.pop()
                if curr != '[':
                    return False
            i += 1
        
        if len(stack) > 0:
            return False
        return True
            