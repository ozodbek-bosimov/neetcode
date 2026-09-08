class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 101
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
            
            if min_price > prices[i]:
                min_price = prices[i]
        
        return max_profit