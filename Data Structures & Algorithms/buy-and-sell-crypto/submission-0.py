# T: O(N)
# S: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_min = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            curr_profit = prices[i] - buy_min
            if curr_profit > max_profit:
                max_profit = curr_profit
            
            if prices[i] < buy_min:
                buy_min = prices[i]
        
        return max_profit
