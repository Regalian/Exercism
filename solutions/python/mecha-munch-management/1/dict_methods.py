"""Functions to manage a users shopping cart items."""

from collections import Counter, defaultdict
from enum import Enum
from typing import Iterable

OUT_OF_STOCK: str = "Out of Stock"
MISSING_AISLE: tuple[str, bool] = ("Unknown", False)


class ErrorMsg(Enum):
    NOT_ITERABLE = "{} must be iterable"
    NOT_DICT = "{} must be a dictionary"


def add_item(
    current_cart: dict[str, int], items_to_add: Iterable[str]
) -> dict[str, int]:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    :raises: TypeError if items_to_add is not iterable or current_cart is not a dictionary.
    """
    if not isinstance(current_cart, dict):
        raise TypeError(ErrorMsg.NOT_DICT.value.format("current_cart"))
    if isinstance(items_to_add, str):
        normalized: list[str] = [items_to_add]
    else:
        normalized: Iterable[str] = items_to_add

    try:
        item_counts: Counter[str] = Counter(normalized)
        for item in item_counts:
            current_cart[item] = current_cart.get(item, 0) + item_counts[item]
    except TypeError:
        raise TypeError(ErrorMsg.NOT_ITERABLE.value.format("items_to_add"))

    return current_cart


def read_notes(notes: Iterable[str]) -> dict[str, int]:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    current_cart: dict[str, int] = defaultdict(int)
    try:
        for item in notes:
            current_cart[item] += 1
    except TypeError:
        raise TypeError(ErrorMsg.NOT_ITERABLE.value.format("notes"))

    return dict(current_cart)


def update_recipes(
    ideas: dict[str, dict[str, int]],
    recipe_updates: Iterable[tuple[str, dict[str, int]]],
) -> dict[str, dict[str, int]]:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas |= dict(recipe_updates)

    return ideas


def sort_entries(cart: dict[str, int]) -> dict[str, int]:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a user's shopping cart dictionary.
    :return: dict - a user's shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(
    cart: dict[str, int], aisle_mapping: dict[str, tuple[str, bool]]
) -> dict[str, tuple[int, str, bool]]:
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - a user's shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    order: dict[str, tuple[int, str, bool]] = {item : [count, *aisle_mapping.get(item, MISSING_AISLE)] for item, count in cart.items()}
    return dict(sorted(order.items(), reverse=True))


def update_store_inventory(
    fulfillment_cart: dict[str, tuple[int, str, bool]],
    store_inventory: dict[str, tuple[int | str, str, bool]],
) -> dict[str, tuple[int | str, str, bool]]:
    """Update store inventory levels with user order.

    :param fulfillment_cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for item, (quantity, _, _) in fulfillment_cart.items():
        try:
            current_stock = store_inventory[item][0]
            if current_stock == OUT_OF_STOCK:
                continue

            current_stock = int(current_stock)
            store_inventory[item][0] = current_stock - quantity if current_stock > quantity else OUT_OF_STOCK
        except KeyError: # Ignore any items in the fulfillment class that are not recodgnised
            continue

    return store_inventory
