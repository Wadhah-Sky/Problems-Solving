"""

    Write a function that takes in an adjacency list of undirected graph, the
    function should return the number of the connected components in the graph.

    adjacency_list = [ [False, False, True, False],
                       [False, False, False, True],
                       [True, False, False, False],
                       [False, True, False, False]]

    // Should return 2

"""

import edges_list_to_dict


def explore_dfs(graph, node, visited):
    """Method to implement depth first search on given graph in form of
    dictionary"""

    if node in visited:
        return False

    visited.add(node)

    # Loop over the list of dictionary key value until reach the end by visit
    # all neighbors node.
    for neighbor in graph[node]:
        explore_dfs(graph, neighbor, visited)

    # When reach the end of search, the first call of recursive calling will
    # return True
    return True


def connected_components_count(graph, visited):
    """Return the count of connected components in graph, Note that the
    unconnected node count as one and group of connected nodes count as one"""

    # Convert boolean adjacency list into dictionary.
    dic = edges_list_to_dict.convert_boolean_edges_to_dic(graph)

    # Initialize an counter
    count = 0

    # Loop over each key in dictionary
    for node in dic:
        # Whenever our dfs search method return true, increase the counter
        if explore_dfs(dic, node, visited):
            count += 1

    return count


adjacency_list = [[False, True, True, False],
                  [True, False, False, True],
                  [True, False, False, False],
                  [False, True, False, False]]

# We use set because searching efficiency for any value is O(1)
visited_list = set()

print(connected_components_count(adjacency_list, visited_list))
