#!/usr/bin/python

import argparse

def find_max_profit(prices):
    # pass
    # solution 1: starting with smallest:
    # starting max profit and current smallest number at zero
    max_profit = -float('inf')

    smallest_number = prices[0]
    valid_smallest_numbers = prices[:-1]
    # loop through each price in list
    print(f"prices: {prices}")
    print(f"valid_smallest_numbers: {valid_smallest_numbers}")

    for i, v in enumerate(valid_smallest_numbers):
    # for v in valid_smallest_numbers:
    #   perhaps except for last price
    #   keep track of smallest number as you go through
    #   if i is less than current smallest number, set i to current smallest number
        # print(f"")
        right = []
        print(f"right BEFORE: {right}")
        if v < smallest_number:
            print(f"v in first if: {v}")
            smallest_number = v
            print(f"new smallest_number: {smallest_number}")
            # right = prices[smallest_number:]
            right = prices[i+1:]
            print(f"right AFTER: {right}")

    #     then loop through each price to the right of the smallest number, including last
            for n in right:
    #           set difference = subtract current smallest number from i
                print(f"n: {n}")
                difference = n - smallest_number
    #           if difference is more than current max profit
                print(f"difference: {difference}")
                print(f"current max_profit: {max_profit}")
                if difference > max_profit:
    #             set as new max profit
                    max_profit = difference
                    print(f"new max_profit: {max_profit}")
            # return max_profit
    #   return the max profit
    return max_profit

print(find_max_profit([1050, 270, 1540, 3800, 2]))

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))