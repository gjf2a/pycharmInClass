from typing import List

def add_to(nums: List[int], n: int):
    for i in range(len(nums)):
        nums[i] = nums[i] + n


def added_to(nums: List[int], n: int) -> List[int]:
    result = []
    for i in range(len(nums)):
        result.append(nums[i] + n)
    return result


def evens_only(nums: List[int]) -> List[int]:
    result = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result


def even_indices_only(nums: List[int]) -> List[int]:
    result = []
    for i in range(0, len(nums), 2):
        result.append(nums[i])
    return result


def first_three(s: str) -> str:
    result = ""
    i = 0
    while i < len(s):
        if s[i] == 'a' or s[i] == 'b' or s[i] == 'c':
            result += s[i]
        i += 1
    return result


def index_of(nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return None


def main():
    nums = []
    done = False
    while not done:
        request = input("Do you want to (1) add a number (2) find a number (3) quit")
        if request == '1':
            n = int(input("enter a number: "))
            nums.append(n)
        elif request == '2':
            n = int(input("What number are you looking for? "))
            location = index_of(nums, n)
            if location is None:
                print("Sorry, your number is not present.")
            else:
                print(f"Your number is at index {location}.")
        elif request == '3':
            done = True


def get_numbers(n: int) -> List[int]:
    result = []
    for i in range(n):
        value = int(input("Enter an integer: "))
        result.append(value)
    return result