"""
Given a binary array, find the maximum number of consecutive 1s in this array.
"""
G_FLAG = 1

class Solution:
    def consecutive_one(self, array):
        if len(array) == 0:
            return array

        max_one = 0
        current_one_count = 0

        for i in range(0, len(array)):
            if array[i] == 1:
                current_one_count += 1
                if current_one_count > max_one:
                    max_one = current_one_count
            else:
                current_one_count = 0
        return max_one 

    def even_count(self, array):
        if len(array) == 0:
            return array

        count = 0

        for num in array:
            if len(str(num)) % 2 == 0:
                count += 1

        return count

    def square_array(self, nums):
        pass

if __name__ == "__main__":
    sol = Solution()

    if not G_FLAG:
        test_consecutive = [
            ([1,1,0,1,1,1], 3),
            ([1,0,1,1,0,1], 2)
        ]
        for array in test_consecutive:
            count = sol.consecutive_one(array[0])
            print(True if count == array[1] else False)

        test_consecutive = [
            [12,345,2,6,7896],
            [555,901,482,1771]
        ] 

        for array in test_consecutive:
            print(sol.even_count(array))

    
    
    


