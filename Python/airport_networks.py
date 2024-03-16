"""

    An airport authority suggested a comprehensive airport network to
    facilitate increased connectivity and smoother logistics. This requires
    adding new flight connections to airport networks. Airports and flight
    connections are represented by a boolean matrix. Airports are represented
    by numbers 0, 1, 2, and so on. So, if airport '0' is connected via a flight
    with airport '1' then elements [0] [1] and [1][0] will have the value True,
    or False if there is no flight connectivity. All flights are
    bi-directional.
    The function get_count accepts a two-dimensional array matrix. The function
    should efficiently calculate and return the number of new flight
    connections so that all airports are reachable from every other airport
    directly.
    Airports with adjacent numbers (e.g., 2 and 3) are near each other and
    connected by other means of transportation. Hence, management has asked to
    avoid new flight connections between immediately adjacent airports. The
    first and last airports are not adjacent.

    The following diagram show to you connection between airports where (==)
    means existing connections, while (--) means new connections:

    0 ==== 1
    2 ==== 3

    0 ---- 2
    0 ---- 3
    0 ---- 4

    1 ---- 3
    1 ---- 4

    2 ---- 4

    For example, the following code should print 6:

    matrix = [
        [False, True, False, False, False],
        [True, False, False, False, False],
        [False, False, False, True, False],
        [False, False, True, False, False],
        [False, False, False, False, False]]

    >> print(get_count (matrix)) # should print 6

"""


def get_count(self):
    return None


matrix = [
        [False, True, False, False, False],
        [True, False, False, False, False],
        [False, False, False, True, False],
        [False, False, True, False, False],
        [False, False, False, False, False]]

print(get_count(matrix))  # should print 6
