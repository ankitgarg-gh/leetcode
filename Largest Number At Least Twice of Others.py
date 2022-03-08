'''747. Largest Number At Least Twice of Others
Easy

635

745

Add to List

Share
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.



Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
Example 3:

Input: nums = [1]
Output: 0
Explanation: 1 is trivially at least twice the value as any other number because there are no other numbers.


Constraints:

1 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique.'''


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 0
        m = max(nums)
        for num in nums:
            if num != m and (2 * num) > m:
                return -1
        for idx in range(len(nums)):
            if nums[idx] == m:
                return idx
        return -1


print(Solution().dominantIndex([3, 6, 1, 0]))
print(Solution().dominantIndex([1, 2, 3, 4]))
print(Solution().dominantIndex([1]))