import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,time in times:
            graph[u].append((v,time))
            
        min_times = {}
        min_heap = [(0,k)] # Total time from source to destination, node
        
        while min_heap:
            time_k_to_i,i = heapq.heappop(min_heap)
            if i in min_times:
                continue
            min_times[i] = time_k_to_i
            
            for nei,nei_time in graph[i]:
                if nei not in min_times:
                    heapq.heappush(min_heap,(time_k_to_i + nei_time,nei))
        
        if len(min_times) == n:
            return max(min_times.values())
        else:
            return -1
    
    # TC : O(V+E log V)
    # SC : O(V+E)
            