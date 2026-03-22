"""
Problem: The Smart Perfume Reseller (Best Time to Buy and Sell Stock II)

Description:
You are given an integer array `prices` where `prices[i]` is the price of a rare perfume bottle on the `i`th day.
Your objective is to find the maximum profit you can achieve.

Rules & Constraints:
1. Multiple Transactions: You may complete as many transactions as you like (i.e., buy one and sell one multiple times).
2. Holding Constraint: You may not engage in multiple transactions simultaneously (i.e., you must sell the perfume before you buy again).

Examples:
- Example 1:
  Input: prices = [7, 1, 5, 3, 6, 4]
  Output: 7
  Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
  Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
  Total profit is 4 + 3 = 7.

- Example 2:
  Input: prices = [1, 2, 3, 4, 5]
  Output: 4
  Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.

- Example 3:
  Input: prices = [7, 6, 4, 3, 1]
  Output: 0
  Explanation: There is no way to make a positive profit, so we never buy the perfume to achieve the maximum profit of 0.

"""

def input_perfume_list():
    print("Enter the perfume prices every day:")
    perfume_price_list=list(map(int,input().split()))
    return perfume_price_list

def max_profit(prices):
    profit=0
    days=len(prices)
    for day in range(days-1):
        if(prices[day+1]>prices[day]):
            profit+=prices[day+1]-prices[day]
    
    return profit

if __name__ == "__main__":
    print("---The Smart Perfume Reseller---")
    daily_prices = input_perfume_list()
    total_profit = max_profit(daily_prices)
    print(f"\nMaximum Profit you can make: {total_profit}")







    
