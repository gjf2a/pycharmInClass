from typing import List

## Accumulation

def factorial(n: int) -> int:
    product = 1
    for i in range(2, n + 1, 1):
        product *= i
    return product


def summation(n: int) -> int:
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


## Map
## * Given a sequence, create a new sequence of the same length
##   with each element altered in some way.
def n_added_to(nums: List[int], n: int) -> List[int]:
    result = []
    for i in range(len(nums)):
        result.append(nums[i] + n)
    return result

def string_shifted(s: str) -> str:
    result = ""
    for i in range(len(s)):
        result += chr(ord(s[i]) + 1)
    return result

## Filter
## * Given a sequence, create a new sequence retaining
##   only the elements that meet some criterion.

def positive_only(nums: List[int]) -> List[int]:
    positives = []
    for i in range(len(nums)):
        if nums[i] > 0:
            positives.append(nums[i])
    return positives

def positive_only_short(nums: List[int]) -> List[int]:
    positives = []
    for num in nums:
        if num > 0:
            positives.append(num)
    return positives

def vowels_only(s: str) -> str:
    vowels = ''
    for i in range(len(s)):
        if s[i] in 'aeiou':
            vowels += s[i]
    return vowels

def vowels_only_short(s: str) -> str:
    vowels = ''
    for letter in s:
        if letter in 'aeiou':
            vowels += letter
    return vowels

## More general accumulation with a list

def list_sum(nums: List[int]) -> int:
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    return sum

