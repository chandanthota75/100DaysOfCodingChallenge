class Solution:
    def shuffleArray(self, arr, n):
        insert_position = 1
        pop_position = n // 2

        for _ in range(n // 2):
            arr.insert(insert_position, arr.pop(pop_position))
            pop_position += 1
            insert_position += 2
