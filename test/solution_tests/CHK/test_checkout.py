import random

from solutions.CHK import checkout_solution


def test_invalid_inputs():
    assert checkout_solution.checkout(0) == -1
    assert checkout_solution.checkout(object) == -1
    assert checkout_solution.checkout("ABCDEZ") == -1


def test_a_deal():
    assert checkout_solution.checkout("A") == 50
    assert checkout_solution.checkout("A" * 2) == 100
    assert checkout_solution.checkout("A" * 3) == 130
    assert checkout_solution.checkout("A" * 4) == 180
    assert checkout_solution.checkout("A" * 5) == 200
    assert checkout_solution.checkout("A" * 6) == 250
    assert checkout_solution.checkout("A" * 7) == 300
    assert checkout_solution.checkout("A" * 8) == 330
    assert checkout_solution.checkout("A" * 10) == 400
    assert checkout_solution.checkout("A" * 13) == 530


def test_valid_inputs():
    assert checkout_solution.checkout("ABCD") == 115
    assert checkout_solution.checkout("ABCDE") == 155

    assert checkout_solution.checkout("AABCD") == 165
    assert checkout_solution.checkout("AABBCD") == 180
    assert checkout_solution.checkout("AABBBCD") == 210
    assert checkout_solution.checkout("AABBBBCD") == 225
    assert checkout_solution.checkout("AABBBBCDD") == 240
    assert checkout_solution.checkout("AABBBBCDDE") == 280
    assert checkout_solution.checkout("AABBBBCDDEF") == 290

    x = list("AABBBBCDDEF")
    random.shuffle(x)

    assert checkout_solution.checkout("".join(x)) == 290


def test_freebies_e():
    assert checkout_solution.checkout("ABCDE") == 155
    assert checkout_solution.checkout("ABCDEE") == 165
    assert checkout_solution.checkout("ACDEE") == 165
    assert checkout_solution.checkout("ABBCDEE") == 195
    assert checkout_solution.checkout("ABCDEEE") == 205
    assert checkout_solution.checkout("ABCDEEEE") == 245


def test_freebies_f():
    assert checkout_solution.checkout("AF") == 60
    assert checkout_solution.checkout("AFF") == 70
    assert checkout_solution.checkout("AFFF") == 70
    assert checkout_solution.checkout("AFFFF") == 80
    assert checkout_solution.checkout("AFFFFF") == 90
    assert checkout_solution.checkout("AFFFFFF") == 90
    assert checkout_solution.checkout("AFFFFFFF") == 100
    assert checkout_solution.checkout("AFFFFFFFF") == 110
    assert checkout_solution.checkout("AFFFFFFFFF") == 110

