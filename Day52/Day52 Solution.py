
'''
Function Arguments :
        @param  : q ( given queue to be used), k(Integer )
        @return : list, just reverse the first k elements of queue and return new queue
'''

class Solution:
    def modifyQueue(self, q, k):
        return q[:k][::-1] + q[k:]