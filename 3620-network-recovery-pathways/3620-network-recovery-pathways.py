from collections import deque

class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        
        # Build adjacency list
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v, cost in edges:
            adj[u].append((v, cost))
            indegree[v] += 1
        
        # Topological order (Kahn's algorithm)
        queue = deque([i for i in range(n) if indegree[i] == 0])
        topo = []
        indeg_copy = indegree[:]
        while queue:
            u = queue.popleft()
            topo.append(u)
            for v, cost in adj[u]:
                indeg_copy[v] -= 1
                if indeg_copy[v] == 0:
                    queue.append(v)
        
        INF = float('inf')
        
        def feasible(X):
            # Minimum cost to reach each node using only edges with cost >= X
            dist = [INF] * n
            dist[0] = 0
            for u in topo:
                if dist[u] == INF:
                    continue
                if u != 0 and not online[u]:
                    continue  # can't pass through an offline node
                for v, cost in adj[u]:
                    if cost >= X:
                        nd = dist[u] + cost
                        if nd < dist[v]:
                            dist[v] = nd
            return dist[n - 1] <= k
        
        # Without any threshold, is there even a valid path?
        if not feasible(0):
            return -1
        
        # Binary search over distinct edge costs for the largest feasible X
        costs = sorted(set(cost for _, _, cost in edges))
        lo, hi = 0, len(costs) - 1
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(costs[mid]):
                ans = costs[mid]
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans