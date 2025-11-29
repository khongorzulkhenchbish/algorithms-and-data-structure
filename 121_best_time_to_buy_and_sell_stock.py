class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float("inf")
        maxprofit = 0
        for price in prices:
            # if current pointer is greater than min then 
            # compare the difference with the max diff.
            # The loop is forward direction that's how we prevent from 
            # selling before buying
            if (price < minprice):
                minprice=price
            elif (price-minprice > maxprofit):
                maxprofit=price-minprice
        return maxprofit
