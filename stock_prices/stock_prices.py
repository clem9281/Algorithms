#!/usr/bin/python

import argparse


# complexity of n^2 though :(
def find_max_profit(prices):
    # from begining to second to last
    for i in range(len(prices) - 1):
        # from the right of i to the end
        for j in range(i + 1, len(prices)):
            # set max_profit to whatever the buy - sell is on the first pass. We don't want to just initialize at 0 because max_profit can be negative
            profit = prices[j] - prices[i]
            if i == 0 and j == 1:
                max_profit = profit
            elif profit > max_profit:
                max_profit = profit
    return max_profit


if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers", metavar="N", type=int, nargs="+", help="an integer price"
    )
    args = parser.parse_args()
    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers), prices=args.integers
        )
    )

