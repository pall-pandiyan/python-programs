from typing import List, Tuple


def sum_of_two_elements(numbers: List[int], target: int) -> Tuple[int]:
    # This is O(n2) complexity - because of two for loops.

    size: int = len(numbers)
    for x in range(size):
        for y in range(x + 1, size):
            if numbers[x] + numbers[y] == target:
                return (x, y)
    return None


numbers: List[int] = [2, 3, 4, 5, 8]
target: int = 7
print(f"numbers: {numbers} and target: {target}")
print(f"sum_of_two_elements: {sum_of_two_elements(numbers,target)}")
