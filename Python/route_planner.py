"""

    As a part of the route planner, the route_exists method is used as a quick
    filter if the destination is reachable, before using more computationally
    intensive procedures for finding the optimal route.

    The roads on the map are rasterizer and produce a matrix of boolean
    values - True if the road is present or False if it is not. The roads in
    the matrix are connected only if the road is immediately left, right, below
    or above it.

    Finish the route_exists method so that it returns True if the destination
    is reachable or False if it is not. The from_row and from_column parameters
    are the starting row and column in the map_matrix. The to_row and to_column
    are the destination row and column in the map_matrix. The map_matrix
    parameter is the above-mentioned matrix produced from the map.

    For example, for the given rasterizer map, the code below:

    >> map_matrix = [
         [True, False, False],
         [True, True, False],
         [False, True, True]
       ];

    >> route_exists(0, 0, 2, 2, map_matrix)

    should return 'True' since the destination is reachable

"""


class RoutePlanner:
    """
    Class RoutePlanner created to try to pass through a matrix from one index
    to another.
    """

    def __init__(self, matrix: list, to_row: int = 0, to_column: int = 0):
        """
        Args:
          matrix (list): A matrix used to be analyzed.
          to_row (int, optional): A end row index of the path. Default 0.
          to_column (int, optional): A end column index of the path. Default 0.
        """
        self.to_row = to_row
        self.to_column = to_column
        self.matrix = matrix
        self.visited = [[False for _ in range(len(matrix[0]))] for _ in
                        range(len(matrix))]

    def valid_move(self, row: int, column: int) -> bool:
        """
        Checks if the row and column index in the array is a valid index.

        Args:
          row (int): Row index of the matrix.
          column (int): Column index of the matrix.

        Returns:
          (bool): A boolean returns used to return if a position in matrix is
          valid.
        """

        # First check the given row and colum is valid coordination.
        if 0 <= row < len(self.matrix) and 0 <= column < len(self.matrix[0]):
            # Check that the matrix that have been set to current instance is
            # return True for given row and column while it hasn't visited
            # given coordination.
            if self.matrix[row][column] and not self.visited[row][column]:
                return True

        # Otherwise return False.
        return False

    def find_path(self, row: int, column: int) -> bool:
        """
        Try to find a path from one index to another.

        Args:
          row (int): Row index of the matrix.
          column (int): Column index of the matrix.

        Returns:
          (bool): A boolean returns if there is a path to certain positions in
          the matrix.
        """
        # Check current row and column is valid and within matrix coordination
        if not self.valid_move(row, column):
            return False

        # This is the important condition where we return True because current
        # parameter of row and column is same row and column of current route
        # planer instance, which means we reach it successfully.
        if row == self.to_row and column == self.to_column:
            return True

        # Set given row and column as visited in visited matrix.
        self.visited[row][column] = True

        # Run recursive call for x-axis and y-axis in right , left, top and
        # down.
        # Note: Recursive will end the moment we get True which happen when
        #       sending row value is equal self.to_row and column value is
        #       equal to self.to_column, otherwise False because we visit all
        #       nodes and we will get valid_move() with False value.
        return (self.find_path(row - 1, column) or
                self.find_path(row, column - 1) or
                self.find_path(row + 1, column) or
                self.find_path(row, column + 1))


def route_exists(from_row: int, from_column: int, to_row: int, to_column: int,
                 matrix: list) -> bool:
    """
    Try to pass through a matrix from one index to another and returns if there
     is a path to the destination.

    Args:
      from_row (int): A start row index of the path.
      from_column (int): A start column index of the path.
      to_row (int): A end row index of the path.
      to_column (int): A end column index of the path.
      matrix (list): A matrix used to be analyzed.

    Returns:
      path (bool): A boolean variable used to return if a path to the
      destination exists.
    """
    if type(from_row) != int or type(from_column) != int or \
            type(to_row) != int or type(to_column) != int:
        raise Exception("The indexes must be integers!")
    if type(matrix) != list:
        raise TypeError("The matrix must be a list!")
    try:
        # Check that start point and end point is Not False
        if (to_row > len(matrix) - 1) or \
           (to_column > len(matrix[0]) - 1) or \
           not matrix[from_row][from_column] or \
           not matrix[to_row][to_column]:
            return False
    except IndexError:
        raise IndexError("The indexes must be valid indexes!")

    route_planner = RoutePlanner(matrix, to_row, to_column)

    return route_planner.find_path(from_row, from_column)


map_matrix = [
    [True, False, False],
    [True, True, False],
    [False, True, True]
]

print(route_exists(0, 0, 2, 2, map_matrix))
