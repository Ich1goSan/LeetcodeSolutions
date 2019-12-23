def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if(len(strs) == 0):
            return ""
        if(len(strs) == 1):
            return strs[0]
        prefix = strs[1]
        for i in range(len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0:len(prefix)-1]
                if(prefix == ""):
                    return ""
        return prefix