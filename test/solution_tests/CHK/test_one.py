from solutions.CHK import checkout_solution


def test_invalid_inputs():
    assert checkout_solution.checkout(0) == -1
    assert checkout_solution.checkout(object) == -1
    assert checkout_solution.checkout("ABCDE") == -1


def test_valid_inputs():
    assert checkout_solution.checkout("ABCD") == 115
    assert checkout_solution.checkout("AABCD") == 165
    assert checkout_solution.checkout("AAABCD") == 195
    assert checkout_solution.checkout("AAAABCD") == 245
    assert checkout_solution.checkout("AAAAABCD") == 295
    assert checkout_solution.checkout("AAAAAABCD") == 325
    assert checkout_solution.checkout("AAAAAABBCD") == 340

