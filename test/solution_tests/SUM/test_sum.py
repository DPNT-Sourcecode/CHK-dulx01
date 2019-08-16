import pytest

from solutions.SUM import sum_solution


@pytest.mark.parametrize("invalid_value", [
    -1, 101, 1.0, "1", None, object()
])
def test_invalid_inputs(invalid_value):
    # tests invalid inputs on both x and y - 1 is valid

    with pytest.raises(ValueError):
        sum_solution.compute(1, invalid_value)
    with pytest.raises(ValueError):
        sum_solution.compute(invalid_value, 1)


@pytest.mark.parametrize("limit_value,result", [
    (0, 1),
    (100, 101),
])
def test_limit_values(limit_value, result):
    assert sum_solution.compute(1, limit_value) == result
    assert sum_solution.compute(limit_value, 1) == result


class TestSum:
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

