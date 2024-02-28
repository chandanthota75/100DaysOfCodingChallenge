class Solution:
    def match(self, wild, pattern):
        i = j = 0
        w = ""
        while i < len(wild) and j < len(pattern):
            if wild[i] in "*?":
                if wild[i] == "?":
                    w += pattern[j]
                else:
                    while i < len(wild) and wild[i] in "*?":
                        i += 1
                    if i == len(wild):
                        while j < len(pattern):
                            w += pattern[j]
                            j += 1
                    while j < len(pattern):
                        if j < i:
                            w += pattern[j]
                        elif wild[i] != pattern[j]:
                            w += pattern[j]
                        else:
                            break
                        j += 1
                    continue
            elif wild[i] == pattern[j]:
                w += wild[i]
            else:
                return False
            i += 1
            j += 1
        return w == pattern