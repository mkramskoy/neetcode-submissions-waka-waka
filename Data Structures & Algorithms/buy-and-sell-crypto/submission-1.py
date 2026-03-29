class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        bestBuyPrices = [prices[0]]
        currentBestBuyPrice = prices[0]
        for i in range(1, len(prices)):
            currentBestBuyPrice = min(prices[i], currentBestBuyPrice)
            bestBuyPrices.append(currentBestBuyPrice)

        print(bestBuyPrices)

        bestSellPrices = []
        currentBestSellPrice = 0
        for i in reversed(range(len(prices))):
            currentBestSellPrice = max(prices[i], currentBestSellPrice)
            bestSellPrices.insert(0, currentBestSellPrice)

        print(bestSellPrices)

        maxProfit = 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit, bestSellPrices[i]-bestBuyPrices[i])

        return maxProfit

        # Input: prices = [10,1,5,6,7,1]
        # best buy: [10, 1, 1, 1, 1, 1, 1]
        # best sell: [10, 7, 7, 7, 7, 7, 1]