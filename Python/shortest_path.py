"""

    Write a function that takes in a list of edges for undirected graph and two
    nodes (nodeA, nodeB), the function should return the length of the shortest
    path between A and B.
    consider the length as the number of edges in the path, not the number of
    nodes. if there is no path between A and B, then return -1, for example:

    >> edges = [['w', 'x'],
                ['x', 'y'],
                ['z', 'y'],
                ['z', 'v'],
                ['w', 'v']]

    >> print(shortest_path(edges, 'w', 'z')) // should return 2

"""

from collections import deque
import edges_list_to_dict


def shortest_path(edges, node_a, node_b):
    """Method to return shortest path from starting node to desired node using
    breadth first search"""

    graph = edges_list_to_dict.convert_named_edges_to_dic(edges)

    visited = set(node_a)

    # Define deque object as list of lists where first element represent node
    # and second represent its distance from starting point.
    queue = deque([[node_a, 0]])

    # Loop until the queue is empty
    while len(queue) > 0:
        # Remove (pop) the first entered element (which is list of node and its
        # distance) from queue.
        current, distance = queue.pop()

        # Check if current element is the same as the wanted one, then return
        # the distance value.
        if current == node_b:
            return distance

        # In case current node is not the wanted one, loop over neighbors of
        # current element of queue.
        for neighbor in graph[current]:
            if neighbor not in visited:
                # Add current value of neighbor in visited set.
                visited.add(neighbor)
                # insert on the left side of queue.
                # Note: if you use append method will change the concept of
                #       search to be depth first search and queue will be as
                #       stack.
                queue.insert(0, [neighbor, distance + 1])

    return -1


edges = [['w', 'x'],
         ['x', 'y'],
         ['z', 'y'],
         ['z', 'v'],
         ['w', 'v']]

print(shortest_path(edges, 'w', 'z'))  # should return 2
print(shortest_path(edges, 'w', 'j'))  # should return -1
print(shortest_path(edges, 'w', 'y'))  # should return 2
