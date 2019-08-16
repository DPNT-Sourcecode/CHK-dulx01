import random

from solutions.CHK import checkout_solution


def test_invalid_inputs():
    assert checkout_solution.checkout(0) == -1
    assert checkout_solution.checkout(object) == -1
    assert checkout_solution.checkout("ABCDEF") == -1


def test_valid_inputs():
    assert checkout_solution.checkout("ABCD") == 115
    assert checkout_solution.checkout("ABCDE") == 155

    assert checkout_solution.checkout("A") == 50
    assert checkout_solution.checkout("A" * 2) == 100
    assert checkout_solution.checkout("A" * 3) == 130
    assert checkout_solution.checkout("A" * 4) == 180
    assert checkout_solution.checkout("A" * 5) == 200
    assert checkout_solution.checkout("A" * 6) == 250
    assert checkout_solution.checkout("A" * 7) == 300
    assert checkout_solution.checkout("A" * 8) == 330


    # assert checkout_solution.checkout("AABCD") == 165
    # assert checkout_solution.checkout("AAABCD") == 195
    # assert checkout_solution.checkout("AAAABCD") == 245
    # assert checkout_solution.checkout("AAAAABCD") == 295
    # assert checkout_solution.checkout("AAAAAABCD") == 325
    # assert checkout_solution.checkout("AAAAAABBCD") == 340
    # assert checkout_solution.checkout("AAAAAABBBCD") == 370
    # assert checkout_solution.checkout("AAAAAABBBBCD") == 385
    # assert checkout_solution.checkout("AAAAAABBBBCDD") == 400
    #
    # x = list("AAAAAABBBBCDD")
    # random.shuffle(x)
    #
    # assert checkout_solution.checkout("".join(x)) == 400


