"""

    Write a method that take dictionary of adjacency list of undirected graph
    and return the size of the largest connected component.

    dic = {
      '0': ['1', '2'],
      '1': ['0', '2'],
      '2': ['0', '1'],
      '3': ['4'],
      '4': ['3']
    }

    // should return 3 which is the largest count of nodes that are connected

"""


def explore_dfs(graph, node, visited, count):
    """Method to implement depth first search on given graph in form of
    dictionary"""

    if node not in visited:
        visited.add(node)
        count += 1

        for neighbor in graph[node]:
            count = explore_dfs(graph, neighbor, visited, count)

    return count


def largest_connected_component(graph):
    """Return the size of the largest connected component"""

    count = 0
    visited = set()

    for node in graph:

        return_val = explore_dfs(graph, node, visited, 0)

        if return_val > count:
            count = return_val

    return count


dic = {
      '0': ['1', '2'],
      '1': ['0', '2'],
      '2': ['0', '1'],
      '3': ['4'],
      '4': ['3']
    }

dic_2 = {
      '0': ['1', '3'],
      '1': ['0', '2'],
      '2': ['1', '3'],
      '3': ['0', '2'],
      '4': ['5', '6'],
      '5': ['4', '6'],
      '6': ['5', '4']
    }

# Test one
print(largest_connected_component(dic))

# Test two
print(largest_connected_component(dic_2))
