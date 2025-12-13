class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        inf = float('inf')
        prices = [inf]*n
        prices[src] = 0
        
        for i in range(k + 1):

            temp_prices = list(prices)
            
            for  (u, v, p) in flights:
                if (temp_prices[u] != inf):
                    if temp_prices[u] + p <= prices[v]:
                        prices[v] = temp_prices[u] + p
                
        return prices[dst] if prices[dst] != inf else -1