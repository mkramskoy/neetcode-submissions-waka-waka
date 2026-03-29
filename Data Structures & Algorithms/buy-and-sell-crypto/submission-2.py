class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        bestBuyPrices = [prices[0]]
        currentBestBuyPrice = prices[0]
        for i in range(1, len(prices)):
            currentBestBuyPrice = min(prices[i], currentBestBuyPrice)
            bestBuyPrices.append(currentBestBuyPrice)

        maxProfit = 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit, prices[i]-bestBuyPrices[i])

        return maxProfit