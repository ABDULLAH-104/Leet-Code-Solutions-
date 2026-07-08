import heapq

class Solution:
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])
        
        # cost[i][j] = minimum health lost to reach cell (i, j)
        cost = [[float('inf')] * n for _ in range(m)]
        cost[0][0] = grid[0][0]  # if starting cell itself is unsafe, cost starts at 1
        
        # min-heap: (total_cost_so_far, row, col)
        heap = [(cost[0][0], 0, 0)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while heap:
            curr_cost, r, c = heapq.heappop(heap)
            
            # if we already found a cheaper way here, skip
            if curr_cost > cost[r][c]:
                continue
            
            # reached destination
            if r == m - 1 and c == n - 1:
                return health - curr_cost >= 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = curr_cost + grid[nr][nc]
                    if new_cost < cost[nr][nc]:
                        cost[nr][nc] = new_cost
                        heapq.heappush(heap, (new_cost, nr, nc))
        
        return health - cost[m - 1][n - 1] >= 1