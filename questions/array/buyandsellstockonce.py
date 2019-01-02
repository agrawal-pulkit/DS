"""
Write a program that takes an array denoting the daily stock price, and retums the maximum profit
that could be made by buying and then selling one share of that stock. There is no need to buy if
no profit is possible.
Hint:ldentifying the minimum and maximum is not enough since the minimum may appear after the maximum
height. Focus on valid differences
"""

def buyAndSellStockOnce(A):
    min_price_so_far, max_profit = float('inf'), 0.0

    for price in A:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    
    return max_profit

# print(buyAndSellStockOnce([310,370,275,275,200,260,270,230,230,230]))


"""
For example/ suppose the input array is <12,11.,1.3,9,12,8,14,1,3,15). Then the most profit that
can be made with a single buy and sell by Day I (inclusive) is F = (0,0,2,2,3,3,6,6,7). Working
backwards, the most profit that can be made with a single buy and sell on or after Day i is
B = (7,7,7,7,7,7,2,2,0). To combine these two, we compute Mlil = f[i- 1] + B[i], where F[-1]
is taken to be 0 (since the second buy must happen strictly after the first sell). This yields M =
<7,7,7,9,9,10,5,8,6), i.e., the maximum profit is 10
"""
def buyAndSellStockTwice(A):
    print(A)
    min_price_so_far, max_total_profit = float('inf'), 0.0
    max_profit_first = [0]*len(A)

    for i,price in enumerate(A):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        max_profit_first[i] = max_total_profit
    
    max_price_so_far = float('-inf')
    for i,price in reversed(list(enumerate(A[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(max_total_profit, max_price_so_far -price + max_profit_first[i-1])  

    return max_total_profit
# print(buyAndSellStockTwice([10,370,275,275,200,260,270,230,230,400]))



"""
Write a Program to compute the maximum profit that can be made by buying and selling a share k
times over a given day range. Your program takes k and an array of daily stock prices as input.
complexity: O(kn)
"""
def buyAndSellStockktimes(prices , k) :
    if not k:
        return 0.0
    elif 2 * k >= len(prices):
        return sum(max(0, b - a) for a, b in zip(prices[:-1], prices[1:]))
    min_prices, max_profits = [float('inf')] * k, [0] * k
    for price in prices:
        for i in reversed(list(range(k))) :
            print(max_profits, min_prices)
            max_profits[i] = max(max_profits[i], price - min_prices[i])
            min_prices[i] = min(min_prices[i] ,
            price - (0 if i == 0 else max_profits[i - 1]))
    return max_profits[- 1]

print(buyAndSellStockktimes([10,370,275,275,200,260,270,230,230,400], 2))
