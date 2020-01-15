def wordPattern(self, pattern: str, str: str) -> bool:
    m = {}
    words = str.split()
        
    if len(pattern) != len(words):
        return False
        
    result = True
        
    for i in range(len(pattern)):
        if pattern[i] not in m:
            if words[i] in m.values():
                return False
            m[pattern[i]] = words[i]
            
        elif m[pattern[i]] != words[i]:
                result = False
                    
    return result