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

    for product, count in products.items():
        if product in DEALS:
            deal_num, deal_price = DEALS[product]

            if count >= deal_num:
                deals = count // deal_num
                price += deals * deal_price
                count -= deals * deal_num

        price += PRICE_TABLE[product] * count

    return price
