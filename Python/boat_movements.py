
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


def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):

    return False


game_matrix = [
    [False, False, True, True, False],
    [False, True, True, False, False],
    [False, False, True, True, False],
    [False, True, False, True, False],
    [False, False, True, False, False]
]

# print(can_travel_to(game_matrix, 2, 2, 0, 2))
# print(can_travel_to(game_matrix, 2, 2, 2, 1))
# print(can_travel_to(game_matrix, 2, 2, 2, 3))
# print(can_travel_to(game_matrix, 2, 2, 1, 1))
