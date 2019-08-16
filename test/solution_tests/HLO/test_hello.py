import pytest

from solutions.HLO import hello_solution

def test_hello():
    assert hello_solution.hello("Thomas") == "Hello, Thomas!"

def test_invalid_input():
    with pytest.raises(ValueError):
        hello_solution.hello(1)
