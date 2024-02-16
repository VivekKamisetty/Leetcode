#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

        """
        max_profit = 0
        n = len(prices)

        for buy in range(n):
            for sell in range(buy+1, n):
                max_profit = max(max_profit, prices[sell] - prices[buy])
        return max_profit
        """

        """     
        maxp = 0

       for buy in range(len(prices)):
            for sell in range(buy, len(prices)):
                if prices[sell] - prices[buy] > 0:
                    diff = prices[sell] - prices[buy]
                    if diff > maxp:
                        maxp = diff
        return maxp
        
        """
"""        l, r = 0, len(prices) - 1
        max_profit = 0
        def profit(l,r):
            return prices[r] - prices[l]

        if len(prices) == 1:
            return 0
        while l < r:
            max_profit = max(max_profit, profit(l,r), profit(l+1,r), profit(l,r-1))
            l+=1
            r-=1
        return max_profit"""
