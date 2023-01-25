import sys


def tsort(edge_list: list[list[str]]) -> list[str]:
    """Performs a topological sort of the given graph.

    The graph is specified as a list of edges, where each edge is a list
    of two vertices.  The result will be a list of the vertices in
    topological sorted order.

    For example:

    #>>> print('\n'.join(tsort([['101', '202'], ['202', '203']])))
    101
    202
    203

    Args:
        edge_list: the graph to be topologically sorted, given as a list
            of edges.

    Returns:
        a list of the vertices in a topological ordering for the given
        graph

    Raises:
        ValueError:
            if the graph contains a cycle (isn't acyclic) with the
            message, "input contains a cycle"
    """
    adjacency = {}
    indegrees = {}

    for edge in edge_list:
        adjacency[edge[0]] = []
        adjacency[edge[1]] = []
        indegrees[edge[0]] = 0
        indegrees[edge[1]] = 0

    for edge in edge_list:
        adjacency[edge[0]].append(edge[1])
        if edge[1] in indegrees:
            indegrees[edge[1]] += 1

    edge_stack = []
    for edge in indegrees:
        if indegrees[edge] == 0:
            edge_stack.append(edge)

    tsort_list = []
    while len(edge_stack) != 0:
        vertex = edge_stack.pop()

        tsort_list.append(vertex)
        for value in adjacency[vertex]:
            indegrees[value] -= 1
            if indegrees[value] == 0:
                edge_stack.append(value)

    if len(adjacency) != len(tsort_list):
        raise ValueError("input contains a cycle")

    return tsort_list


# NOTE: You should not modify the main function.  You also don't need
# to write tests for the main function.
def main(argv: list[str]) -> None:
    if len(argv) != 2:
        print('usage: python3 tsort.py <filename>', file=sys.stderr)
        sys.exit(1)

    with open(argv[1]) as file:
        edge_list = [line.split() for line in file]

    print('\n'.join(tsort(edge_list)))


if __name__ == '__main__':
    main(sys.argv)
