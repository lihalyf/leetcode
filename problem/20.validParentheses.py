class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapper = {"(" : ")", "[" : "]", "{" : "}"}
        for i in range(len(s)):
            if s[i] in ["(", "[", "{"]:
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            elif s[i] == mapper[stack.pop()]:
                continue
            else:
                return False
        if len(stack) == 0:
            return True
        return False
        
