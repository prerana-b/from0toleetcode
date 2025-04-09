class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        conversion = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        i = 0
        while i<len(s):
            one = conversion[s[i]]
            if i+1<len(s):
                two = conversion[s[i+1]]
                if(two>one):
                    number = number - one + two 
                    i+= 1
                else: 
                    number = number + one
            else: 
                number = number + one
            i+=1
        return number
