from typing import List
from utils import read, write


def dp_change(money: int, coins: List[int]) -> int:
    min_amount_coins_for_change = [10 ** 9] * (money + 1)
    for cur_val in range(1, money + 1):
        if cur_val in coins:
            min_amount_coins_for_change[cur_val] = 1
        else:
            for coin in coins:
                if cur_val >= coin:
                    min_amount_coins_for_change[cur_val] = min(
                        min_amount_coins_for_change[cur_val],
                        min_amount_coins_for_change[cur_val - coin] + 1)
    ans = min_amount_coins_for_change[money]
    if ans == 10 ** 9:
        return -1
    return ans


def main():
    money, *coins, = read()
    money, coins = money[0], coins[0]
    ans = dp_change(money, coins)
    if ans == -1:
        write("IMPOSSIBLE")
    else:
        write(ans)


if __name__ == "__main__":
    main()
