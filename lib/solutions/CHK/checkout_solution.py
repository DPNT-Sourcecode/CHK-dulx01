from collections import Counter

PRICE_TABLE = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21,
}

DEALS = {
    "A": [
        (5, 200),
        (3, 130),
    ],
    "B": [
        (2, 45)
    ],
    "H": [
        (10, 80),
        (5, 45),
    ],
    "K": [
        (2, 120),
    ],
    "P": [
        (5, 200),
    ],
    "Q": [
        (3, 80),
    ],
    "V": [
        (3, 130),
        (2, 90),
    ]
}

FREEBIES = {
    "E": [
        (2, "B", 1),  # for 2E get 1B for free
    ],
    "F": [
        (2, "F", 1),
    ],
    "N": [
        (3, "M", 1),
    ],
    "R": [
        (3, "Q", 1),
    ],
    "U": [
        (3, "U", 1),
    ]
}

GROUP_DEALS = [
    ("STXYZ", 3, 45),  # buy three of STXYZ for 45
]


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
                required_count = deal_count if freebie_product != what else deal_count + how_many

                if count >= deal_count:
                    freebie_deals = count // required_count
                    free_units = freebie_deals * how_many

                    if what in products:
                        products[what] = max(0, products[what] - free_units)

    for group_deal, group_count, group_deal_price in GROUP_DEALS:
        group_products = list(group_deal)

        # sort products from most expensive
        group_products.sort(key=lambda x: PRICE_TABLE[x], reverse=True)

        total_from_group = sum(products.get(k, 0) for k in group_products)

        if total_from_group >= group_count:
            deals = total_from_group // group_count
            price += deals * group_deal_price
            remove_products = deals * group_count



    for product, count in products.items():
        if product in DEALS:
            for deal_num, deal_price in DEALS[product]:
                if count >= deal_num:
                    deals = count // deal_num
                    price += deals * deal_price
                    count -= deals * deal_num

        price += PRICE_TABLE[product] * count

    return price


