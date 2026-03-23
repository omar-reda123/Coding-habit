"""
Problem: The Car Budget Matcher (Two Sum)

Description:
Given an array of integers `prices` and an integer `target`, return the indices of the two cars such that they add up to `target`.

Rules & Constraints:
1. You may assume that each input would have exactly one solution.
2. You may not use the same car (index) twice.
3. You can return the answer in any order.

Examples:
- Example 1:
  Input: prices = [2, 7, 11, 15], target = 9
  Output: [0, 1]
  Explanation: Because prices[0] + prices[1] == 9, we return [0, 1].

- Example 2:
  Input: prices = [3, 2, 4], target = 6
  Output: [1, 2]

"""

def input_car_data():
    prices = list(map(int, input("Enter car prices separated by space: ").split()))
    target = int(input("Enter the target budget: "))
    return prices, target

def find_car_pair(prices, target):
    seen_prices = {} 
    for i in range(len(prices)):
        complement=target-prices[i]
        if(complement in seen_prices):
            return seen_prices[complement],i
        else:
            seen_prices[prices[i]]=i
    return []
           

            
    
    
if __name__ == "__main__":
    print("---The Car Budget Matcher---")
    car_prices, target_budget = input_car_data()
    result = find_car_pair(car_prices, target_budget)
    if result:
        print(f"\nMatch found at indices: {result}")
    else:
        print("\nNo matching pair found for this budget.")