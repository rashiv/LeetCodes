"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Example 1:

Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Example 2:

Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"""

#YOUR CODE GOES HERE
def max_profit_helper(price):
    max_out = 0 min_price = price[0]
    # efficient O(N) way by keeping track of biggest peak and valley
    if(len(price) < 2):
        return max_out
    for i in range(1, len(price)):
        if(min_price > price[i]):
            min_price = price[i]
        if(max_out < price[i] - min_price):
            max_out = price[i] - min_price
    
    return max_out


##DON"T CHANGE THIS
def max_profit(price):
    return max_profit_helper(price)
