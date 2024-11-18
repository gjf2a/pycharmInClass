from functools import total_ordering
from typing import List

def loop_sum_while(nums: List[int]) -> int:
    total = 0
    i = 0
    while i < len(nums):
        total += nums[i]
        i += 1
    return total


def loop_sum_for_range(nums: List[int]) -> int:
    total = 0
    for i in range(0, len(nums), 1):
        total += nums[i]
    return total


def loop_sum_recursive_start(nums: List[int]) -> int:
    return loop_sum_recursive_1(nums, 0, 0)


def loop_sum_recursive_1(nums: List[int], i: int, total: int) -> int:
    if i == len(nums):
        # Base case
        return total
    else:
        # Recursive case
        # How does this move us closer to the base case?
        return loop_sum_recursive_1(nums, i + 1, total + nums[i])


def loop_sum_while_2(nums: List[int]) -> int:
    total = 0
    while len(nums) > 0:
        total += nums[0]
        nums = nums[1:]
    return total

def loop_sum_recursive_2(nums: List[int]) -> int:
    if len(nums) == 0:
        # Base case: empty list
        return 0
    else:
        # Recursive case
        # Reducing the size of the list by one
        return nums[0] + loop_sum_recursive_2(nums[1:])


def factorial_while(n: int) -> int:
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def factorial_recursive(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)