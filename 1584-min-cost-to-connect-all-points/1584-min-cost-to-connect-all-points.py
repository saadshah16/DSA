import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's Algorithm
        
        n = len(points)
        seen = set()
        min_heap = [(0,0)]
        total_cost = 0
        
        while len(seen) < n:
            dist, i = heapq.heappop(min_heap)
            if i in seen: continue
                
            seen.add(i)
            total_cost += dist
            xi, yi = points[i]
            
            for j in range(n):
                xj , yj = points[j]
                nei_dist = abs(xi-xj) + abs(yi-yj)
                heapq.heappush(min_heap, (nei_dist,j))
                
        return total_cost
    
    # TC: O(n^2 log n)
    # SC: O(n^2)
            
        