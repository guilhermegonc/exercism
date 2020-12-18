from collections import Counter, defaultdict


def total(basket):
    items = Counter(basket)
    price_similar_bags = priorize_similar_bags(items)
    price_max_items = priorize_max_items(items)
    return min([price_max_items, price_similar_bags])


def priorize_similar_bags(items):
    cart = setup_cart(items)
    [fulfill_bags(item, quantity, cart, 'similar_bags') for item, quantity in items.most_common()]
    prices = list_prices_per_bag(cart)
    return sum(prices)


def priorize_max_items(items):
    cart = setup_cart(items)
    [fulfill_bags(item, quantity, cart, 'maximize_items') for item, quantity in items.most_common()]
    prices = list_prices_per_bag(cart)
    return sum(prices)


def setup_cart(items):
    cart = defaultdict(list)
    groups = max(items.values()) if items != Counter() else 0
    [cart[i] for i in range(groups)]
    return sort_bags(cart.items())


def sort_bags(cart, reverse=False):
    return sorted(cart, key=lambda i: len(i[1]), reverse=reverse)


def fulfill_bags(item, quantity, cart, is_max_items):
    is_max_items = is_max_items == 'maximize_items'
    cart = sort_bags(cart, is_max_items)
    return [cart[i][1].append(item) for i in range(quantity)]


def list_prices_per_bag(cart):
    return [set_price(len(items)) for _, items in cart]


def set_price(quantity):
    price = 800 * quantity
    if quantity == 2:
        return price * 0.95
    if quantity == 3:
        return price * 0.90
    if quantity == 4:
        return price * 0.80
    if quantity == 5:
        return price * 0.75
    return price
