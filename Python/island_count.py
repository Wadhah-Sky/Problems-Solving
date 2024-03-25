"""

    Write a method that takes in a grid containing 'W' (means water) and 'L'
    (means land).
    The method should return the number of islands on the grid, an island is
    a vertically or horizontally connected of land.

    >> grid = [['W', 'L', 'W', 'W', 'W'],
               ['W', 'L', 'W', 'W', 'W'],
               ['W', 'W', 'W', 'L', 'W'],
               ['W', 'W', 'L', 'L', 'W'],
               ['L', 'W', 'W', 'L', 'L'],
               ['L', 'L', 'W', 'W', 'W']]

    >> island_count(grid)  # Should return 3
"""


def dfs(grid, row, column):
    """Method to implement depth first search over given row and column in
    grid"""

    if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]) \
            or grid[row][column] == 'W':
        return 0

    grid[row][column] = 'W'

    dfs(grid, row, column - 1)
    dfs(grid, row, column + 1)
    dfs(grid, row - 1, column)
    dfs(grid, row + 1, column)

    return 1


def island_count(grid):
    """Method to count number of connected lands vertically and horizontal"""

    islands = 0
    rows = len(grid)
    columns = len(grid[0])

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 'L':
                islands += dfs(grid, row, column)

    return islands


grid = [['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W']]

print(island_count(grid))
