from typing import List, Tuple, Dict


def sum_of_two_elements(numbers: List[int], target: int) -> Tuple[int]:
    """
    # This is O(n2) complexity - because of two for loops.

    size: int = len(numbers)
    for x in range(size):
        for y in range(x + 1, size):
            if numbers[x] + numbers[y] == target:
                return (x, y)
    return None
    """
    size: int = len(numbers)
    visited_numbers: Dict[int, int] = {}

    for i in range(size):
        diff: int = target - numbers[i]

        # print(f"{visited_numbers=}")
        # print(f"{number=}")
        # print(f"{diff=}")

        # we cannot skip this for some edge cases - numbers = [2,2,3,4], target=4
        # if the element is duplicated, just skip the iteration.
        # if numbers[i] in visited_numbers:
        # continue

        if diff in visited_numbers:
            return (i, visited_numbers[diff])

        visited_numbers[numbers[i]] = i


numbers: List[int] = [2, 2, 3, 4, 5, 8]
target: int = 4
print(f"numbers: {numbers} and target: {target}")
print(f"sum_of_two_elements: {sum_of_two_elements(numbers,target)}")
