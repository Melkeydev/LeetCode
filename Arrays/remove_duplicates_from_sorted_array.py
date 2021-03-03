"""
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums
"""

from collections import Counter

class Solution:
    def remove_duplicates(self, nums)->int:
        dict_nums = {}
        index_list = []
        for num in nums:
            if num not in dict_nums:
                dict_nums[num] = 0
            else:
                index_list.append(num)

        for index_num in index_list:
            nums.remove(index_num)

        return nums


if __name__ == "__main__":
    input_name = [0,0,1,1,1,2,2]
    sol = Solution()
    print(sol.remove_duplicates(input_name))
