"""

    Convert adjacency list of edges to dictionary:

    adjacency_list = [ ['i', 'j'], ['m', 'i'] ]

    dic = {'i': ['j', 'm'], 'j': ['i'], 'm': ['i']}

    OR

    adjacency_list = [ [False, False, True],
                       [False, False, True],
                       [True, True, False]]

    dic = {0: [2], 1: [2], 2: [0, 1]}

"""


def convert_named_edges_to_dic(graph):
    """Get graph of named edges of edges and convert it to dictionary"""

    dic = {}

    for row in graph:
        a, b = row

        if a not in dic:
            dic[a] = []
        if b not in dic:
            dic[b] = []

        dic[a].append(b)
        dic[b].append(a)

    return dic


def convert_boolean_edges_to_dic(graph):
    """Get graph of true/false edges of edges and convert it to dictionary"""

    dic = {}
    index = 0

    for row in graph:
        dic[index] = []

        for i in range(len(row)):

            if row[i]:
                dic[index].append(i)

        index += 1

    return dic


# Here we use __name__ argument to prevent any call from outside this module to
# run it.
if __name__ == "__main__":

    named_adjacency_list = [['i', 'j'], ['m', 'i']]

    print(convert_named_edges_to_dic(named_adjacency_list))

    boolean_adjacency_list = [[False, False, True],
                              [False, False, True],
                              [True, True, False]]

    print(convert_boolean_edges_to_dic(boolean_adjacency_list))
