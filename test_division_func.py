from utils2 import division
import pytest

@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -3, -10)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result
