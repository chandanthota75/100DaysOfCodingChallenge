class Solution:
    def checkPangram(self, s):
        result = set()
        for i in s:
            if i.isalpha():
                result.add(i.upper())
        return len(result) == 26