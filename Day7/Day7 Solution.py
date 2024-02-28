class Solution:
    def sumOfDependencies(self,adj,V):
        return sum([len(e) for e in adj])