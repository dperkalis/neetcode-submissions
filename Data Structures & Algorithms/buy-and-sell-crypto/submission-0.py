class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        CurrentPrice
        NextPrice 
        NextPrice < CurrentPrice, CurrentPrice = NextPrice
        NextPrice > CurrentPrice, Profit = NextPrice-CurrentPrice
        """
        min_price = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > min_price and prices[i] - min_price > profit:
                profit = prices[i] - min_price
            elif prices[i] < min_price:
                min_price = prices[i]

        
        return profit

       
            


            

