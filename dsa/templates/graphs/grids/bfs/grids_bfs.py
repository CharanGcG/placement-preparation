def bfs(start_row, start_col, rows, cols, grid):
    """Performs BFS on a grid starting from the given cell."""
    queue = [(start_row, start_col)]
    visited = set()
    visited.add((start_row, start_col))
    while queue:
        x, y = queue.pop(0)
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = dx + x, dy + y
            if (0 <= nx < rows and 0 <= ny < cols and grid[nx][ny]==1 and (nx, ny) not in visited):
                queue.append((nx,ny))
                visited.add((nx,ny))


def count_components_in_grid(grid):
    """
    Counts the number of connected components in a grid using BFS.
    Each component is defined by adjacent cells with value "1".
    """
    visited = set()
    components = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row,col) not in visited and grid[row][col] == "1":
                components += 1
                bfs(row, col, len(grid), len(grid[0]))
