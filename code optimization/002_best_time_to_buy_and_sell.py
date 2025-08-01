"""
Ref: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
    1 <= prices.length <= 105
    0 <= prices[i] <= 104
"""


def biggest_profit(prices: list[int]) -> int:
    profit: int = 0
    size: int = len(prices)
    if size < 2:
        return profit

    """
    # O(n2) solution
    for x in range(size):
        for y in range(x + 1, size):
            new_profit: int = prices[y] - prices[x]
            if new_profit > profit:
                profit = new_profit
    return profit
    """

    # O(n) solution
    left: int = 0
    for right in range(1, size):
        if prices[left] < prices[right]:
            new_profit: int = prices[right] - prices[left]
            if new_profit > profit:
                profit = new_profit
        else:
            left = right
    return profit


for prices in [7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1]:
    print("prices:", prices)
    print("biggest_profit:", biggest_profit(prices))
    print()
