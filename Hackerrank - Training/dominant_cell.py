def numCells(grid):
    n = len(grid)  # Number of rows
    m = len(grid[0])  # Number of columns
    dominant_count = 0
    
    # Directions for the 8 possible neighbors (up, down, left, right, and the 4 diagonals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    # Function to check if a cell is within the grid boundaries
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    # Loop through each cell in the grid
    for i in range(n):
        for j in range(m):
            cell_value = grid[i][j]
            is_dominant = True
            
            # Check all 8 neighbors
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if is_valid(ni, nj) and grid[ni][nj] >= cell_value:
                    is_dominant = False
                    break
            
            if is_dominant:
                dominant_count += 1

    return dominant_count
