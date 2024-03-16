
"""

    A game grid represents water and land masses. The grid contains a True
    value where it's water and False where it's land.
    A boat can go to the next tile in the left or right directions, or move
    twice in the top and bottom directions. All the tiles in the path must be
    inside the grid and contain water.
    Implement the can_travel_to function, which accepts a grid matrix, starting
    and destination coordinates (row and column), and returns a boolean
    indicating whether a boat can travel between the two points in one step.

    For example, the following code:

    game matrix = [
        [False, False, True, True, False],
        [False, False, True, False, False],
        [False, False, True, True, False],
        [False, True, False, True, False],
        [False, False, True, False, False]
    ]

    print(can_travel_to (game_matrix, 2, 2, 0, 2))
    print(can_travel_to (game_matrix, 2, 2, 2, 1))
    print(can_travel_to (game_matrix, 2, 2, 2, 3))
    print(can_travel_to(game_matrix, 2, 2, 4, 2))

    Should print:

    True
    False
    True
    False

"""


class BoatMovements:
    """Class to simulate boat movements"""

    def __init__(self, matrix, to_row, to_column):
        self.row = to_row
        self.column = to_column
        self.matrix = matrix
        self.visited = [
            [False for _ in range(len(matrix[0]))]
            for _ in range(len(matrix))
        ]

    def valid_move(self, row, column):
        """Method to return True if current move is within the grid and on
        water and not been visited before by current instance (boat)"""

        if 0 <= row < len(self.matrix) and 0 <= column < len(self.matrix[0]):
            if self.matrix[row][column] and not self.visited[row][column]:
                return True

        return False

    def dfs(self, row, column):
        """Method to implement Depth First search for given step coordinates"""

        # Check if current coordinates are valid.
        if not self.valid_move(row, column):
            return False

        # Check if current coordinates (from) are same coordinates of instance
        # (to), then return True.
        if self.row == row and self.column == column:
            return True

        # If none of the conditions above is True, then set current
        # coordinates as visited by instance (boat).
        self.visited[row][column] = True

        # Recursive call that break whenever a True is return
        return (self.dfs(row - 1, column) or
                self.dfs(row, column - 1) or
                self.dfs(row + 1, column) or
                self.dfs(row, column + 1))


def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):
    """Method to check if boatMovements instance is able to travel to given
    coordinates depending on starting point"""

    # Check that:
    # 1- The given coordinates within the grid.
    # 2- Restrict the steps (two when moving top/down and one left/right).
    if (to_row > len(game_matrix) - 1) or \
       (to_column > len(game_matrix[0]) - 1) or \
       (from_row != to_row and abs(to_row - from_row) != 2) or \
       (from_column != to_column and abs(to_column - from_column) != 1):

        return False

    # Check that The start and end coordinates are True, otherwise return False
    if not game_matrix[from_row][from_column] or \
       not game_matrix[to_row][to_column]:
        return False

    # Create a BoatMovements instance and set coordination of the end
    # destination.
    boat_movements = BoatMovements(game_matrix, to_row, to_column)

    # Call dfs method and return its response.
    return boat_movements.dfs(from_row, from_column)


game_matrix = [
        [False, False, True, True, False],
        [False, False, True, False, False],
        [False, False, True, True, False],
        [False, True, False, True, False],
        [False, False, True, False, False]
]

print(can_travel_to(game_matrix, 2, 2, 0, 2))
print(can_travel_to(game_matrix, 2, 2, 2, 1))
print(can_travel_to(game_matrix, 2, 2, 2, 3))
print(can_travel_to(game_matrix, 2, 2, 1, 2))
