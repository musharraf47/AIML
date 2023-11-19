def aStarAlgo(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {}  # store distance from starting node
    parents = {}  # parents contain an adjacency map of all nodes
    # distance of starting node from itself is zero
    g[start_node] = 0
    # start_node is the root node i.e it has no parent nodes
    # so start_node is set to its own parent node
    parents[start_node] = start_node

    def get_neighbors(v):
        if v in Graph_nodes:
            return Graph_nodes[v]
        else:
            return None

    def heuristic(n):
        H_dist = {
            'A': 11,
            'B': 6,
            'C': 99,
            'D': 1,
            'E': 7,
            'G': 0,
        }
        return H_dist[n]

    while len(open_set) > 0:
        n = None

        # node with the lowest f() is found
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n is None:
            print('Path does not exist!')
            return None

        if n == stop_node or Graph_nodes[n] is None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)
            path.reverse()

            print('Path found: {}'.format(path))
            return path

        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None

# Describe your graph here
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}

aStarAlgo('A', 'G')
