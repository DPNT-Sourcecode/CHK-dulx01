from collections import Counter

PRICE_TABLE = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
}

DEALS = {
    "A": [
        (5, 200),
        (3, 130),
    ],
    "B": [
        (2, 45)
    ],
}

FREEBIES = {
    "E": [
        (2, "B", 1),  # for 2E get 1B for free
    ]
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

    for freebie_product, freebie_values in FREEBIES.items():
        if freebie_product in products:
            count = products[freebie_product]
            for deal_count, what, how_many in freebie_values:
                if count > deal_count:
                    freebie_deals = count // deal_count
                    free_units = freebie_deals * how_many

                    if what in products:
                        products[what] = max(0, products[what] - free_units)

    for product, count in products.items():
        if product in DEALS:
            for deal_num, deal_price in DEALS[product]:
                if count >= deal_num:
                    deals = count // deal_num
                    price += deals * deal_price
                    count -= deals * deal_num

        price += PRICE_TABLE[product] * count

    return price



