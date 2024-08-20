# Test the function
def test_find_special_numbers():
    result = find_special_numbers(1000, 2000)
    assert (
        len(result) > 0
    ), "Should find at least one special number in the range 1000-2000"
    for n, x, y, z in result:
        assert 1000 <= n <= 2000, f"Number {n} is out of the specified range"
        assert (
            n == x**3 + 2 * y**3 + 4 * z**3 - 6 * x * y * z
        ), f"Equation doesn't hold for {n}, {x}, {y}, {z}"
    print("All tests passed!")


test_find_special_numbers()
