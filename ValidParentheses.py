class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "{" or i =="[":
                stack.append(i)
            else:
                if len(stack)>0:
                    char = stack.pop()
                    if (i==")" and char!="(") or (i=="}" and char!="{") or (i=="]" and char!="["):
                        return False
                else:
                    return False
        if len(stack)==0:
            return True
        return False 
