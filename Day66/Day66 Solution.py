class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    def fractionalknapsack(self, W,arr,n):
        for item in arr:
            item.ratio = item.value / item.weight
        arr.sort(key=lambda x: x.ratio, reverse=True)

        total_value = 0.0
        current_weight = 0

        for item in arr:
            if current_weight + item.weight <= W:
                total_value += item.value
                current_weight += item.weight
            else:
                remaining_weight = W - current_weight
                fraction = remaining_weight / item.weight
                total_value += fraction * item.value
                break

        return total_value