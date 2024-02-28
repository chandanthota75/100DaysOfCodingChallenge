class Solution:
    def search(self, pat, txt):
        l = []
        i = 0
        while i < len(txt):
            i = txt.find(pat, i)
            if i == -1:
                break
            l.append(i + 1)
            i += 1
                    
        return l