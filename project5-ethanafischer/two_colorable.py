import sys


"""class Vertex:
    def __init__(self, color, adjacencies):
        self.color = color
        self.adjacencies = adjacencies"""


def is_two_colorable(edge_list: list[list[str]]) -> bool:
    """Determines if the given graph is two-colorable.

    The graph is specified as a list of edges, where each edge is a list
    of two vertices.  The result will be True if the given graph is two
    colorable, and False otherwise.

    Args:
        edge_list: the graph to analyze, given as a list of edges

    Returns:
        True if the given graph is two-colorable, False otherwise
    """
    adjacency = {}
    colors = {}

    for edge in edge_list:
        adjacency[edge[0]] = []
        adjacency[edge[1]] = []
        colors[edge[0]] = -1
        colors[edge[1]] = -1

    for edge in edge_list:
        adjacency[edge[0]].append(edge[1])
        adjacency[edge[1]].append(edge[0])

    for i in adjacency:
        if colors[i] == -1:
            if not explore(i, 0, colors, adjacency):
                return False
    return True


def explore(cur_vertex, cur_color, colors, adjacency):
    colors[cur_vertex] = cur_color
    if cur_color == 0:
        opposite_color = 1
    else:
        opposite_color = 0

    for j in adjacency[cur_vertex]:
        if colors[j] == cur_color:
            return False
        elif colors[j] == -1 and not \
                explore(j, opposite_color, colors, adjacency):
            return False
    return True


def main(argv: list[str]) -> None:
    if len(argv) != 2:
        print('usage: python3 two_colorable.py <filename>', file=sys.stderr)
        sys.exit(1)

    with open(argv[1]) as file:
        edge_list = [line.split() for line in file]

    print(is_two_colorable(edge_list))


if __name__ == '__main__':
    main(sys.argv)
