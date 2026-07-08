import heapq
from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        
        # Step 1: Multi-source BFS to find distance to nearest thief for every cell
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
        
        # Edge case: no thieves at all -> safeness is unbounded, but per constraints there's at least one thief usually.
        # If grid[0][0] or grid[n-1][n-1] is a thief cell itself, dist there is 0, handled naturally.
        
        # Step 2: Maximize the minimum safeness along path from (0,0) to (n-1,n-1)
        # Widest path problem using max-heap (like Dijkstra)
        safeness = [[-1] * n for _ in range(n)]
        safeness[0][0] = dist[0][0]
        
        # max-heap simulated with negative values
        heap = [(-dist[0][0], 0, 0)]
        
        while heap:
            neg_val, r, c = heapq.heappop(heap)
            val = -neg_val
            
            if val < safeness[r][c]:
                continue
            
            if r == n - 1 and c == n - 1:
                return val
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    new_val = min(val, dist[nr][nc])
                    if new_val > safeness[nr][nc]:
                        safeness[nr][nc] = new_val
                        heapq.heappush(heap, (-new_val, nr, nc))
        
        return safeness[n - 1][n - 1]