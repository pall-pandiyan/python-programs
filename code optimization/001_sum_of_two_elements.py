"""
Ref: https://leetcode.com/problems/two-sum/description/

1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

Runtime: 4ms Beats 41.92%
Memory: 18.91MB Beats 33.23%

Runtime: 0ms Beats 100.00%
Memory: 18.82MB Beats 50.49%
"""


def sum_of_two_elements(numbers: list[int], target: int) -> tuple[int] | None:
    """
    # This is O(n2) complexity - because of two for loops.
    size: int = len(numbers)
    for x in range(size):
        for y in range(x + 1, size):
            if numbers[x] + numbers[y] == target:
                return (x, y)
    return None
    """
    visited_numbers: dict[int, int] = {}
    for i in range(len(numbers)):
        diff: int = target - numbers[i]
        if diff in visited_numbers:
            return (visited_numbers[diff], i)
        visited_numbers[numbers[i]] = i


for numbers, target in zip(([2, 7, 11, 15], [3, 2, 4], [3, 3]), (9, 6, 6)):
    print(f"numbers: {numbers} and target: {target}")
    print(f"sum_of_two_elements: {sum_of_two_elements(numbers,target)}")
    print()
