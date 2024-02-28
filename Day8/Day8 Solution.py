class Solution:
    def isEulerCircuitExist(self, V, adj):
        degrees = [0] * V
        
        for neighbors in adj:
            for neighbor in neighbors:
                degrees[neighbor] += 1
        
        odd_degree_count = sum(1 for degree in degrees if degree % 2 != 0)
    
        if odd_degree_count == 0:
            return 2
        elif odd_degree_count <= 2:
            return 1
        else:
            return 0