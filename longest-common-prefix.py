class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        normal = strs[0]
        prefix = ""
        for i in normal:
            tempprefix = prefix+i
            count = 0
            for j in range(1,len(strs)):
                if strs[j].startswith(tempprefix):
                    count = count+1
            if count+1 == len(strs):
                prefix = tempprefix
            else:
                break
        return prefix
