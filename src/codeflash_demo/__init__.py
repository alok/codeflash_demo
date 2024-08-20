def hello() -> str:
    return "Hello from codeflash-demo!"


# all numbers 10^19,10^19+10^4 that are of forms x^3 + 2y^3 + 4z^3 - 6xyz

import itertools
from typing import List, Tuple


def find_special_numbers(
    start: int = 10**19, end: int = 10**19 + 10**4
) -> List[Tuple[int, int, int, int]]:
    """
    Find all numbers in the range [start, end] that can be expressed as x^3 + 2y^3 + 4z^3 - 6xyz.

    Args:
        start (int): The start of the range to search (default: 10^19)
        end (int): The end of the range to search (default: 10^19 + 10^4)

    Returns:
        List[Tuple[int, int, int, int]]: A list of tuples (n, x, y, z) where n is the number
        and x, y, z are the values that satisfy the equation.
    """
    results = []

    # Estimate the maximum possible values for x, y, z
    max_value = int((end) ** (1 / 3)) + 1

    for n in range(start, end + 1):
        for x, y, z in itertools.product(range(max_value), repeat=3):
            if x**3 + 2 * y**3 + 4 * z**3 - 6 * x * y * z == n:
                results.append((n, x, y, z))
                break  # Move to the next n once a solution is found

    return results


# Example usage:
special_numbers = find_special_numbers()
print(f"Found {len(special_numbers)} special numbers:")
for n, x, y, z in special_numbers:
    print(f"{n} = {x}^3 + 2*{y}^3 + 4*{z}^3 - 6*{x}*{y}*{z}")

