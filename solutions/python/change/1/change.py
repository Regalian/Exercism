from collections import defaultdict

def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """Find the fewest coins needed to make the target amount.

    Uses dynamic programming to find the fewest coins needed to make the target amount.

    Args:
        coins: A list of coin denominations.
        target: The target amount to make with the coins.
    Returns:
        A list of coin denominations that add up to the target amount.

    Raises:
        ValueError if the target amount cannot be made with the given coins.
        ValueError if the target amount is negative.
    """
    fewest_found = defaultdict()
    fewest_found[0] = []

    def find_fewest(coins: list[int], target: int) -> list[int]:
        if target < 0:
            raise ValueError("target can't be negative")
        best = []

        coins = sorted(coins, reverse=True)
        if target in fewest_found:
            return fewest_found[target]

        min = float('inf')
        for coin in coins:
            if coin <= target:
                try:
                    result:list[int] = find_fewest(coins, target - coin)
                    if len(result) + 1 < min:
                        min = len(result) + 1
                        best = [*result, coin]
                except ValueError:
                    pass
        if not best:
            raise ValueError("can't make target with given coins")
        fewest_found[target] = best
        return best

    return find_fewest(coins, target)
