from collections import Counter

PRICE_TABLE = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

DEALS = {
    "A": (3, 130),
    "B": (2, 45),
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):  # invalid input, wrong type
        return -1

    products = Counter(skus)

    if len(products.keys() - PRICE_TABLE.keys()):  # unknown product
        return -1

    price = 0

    for product, count in 

    raise NotImplementedError()

