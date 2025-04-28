def aStarAlgo(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {}  # Actual distance from start node
    parents = {}  # To keep track of the path
    g[start_node] = 0
    parents[start_node] = start_node

    print(f"Starting A* from '{start_node}' to '{stop_node}'\n")

    while len(open_set) > 0:
        print(f"\nOpen Set: {open_set}")
        n = None
        # Find node with the lowest f() = g() + h()
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        print(f"Selected node with lowest f(n): '{n}' (g={g[n]}, h={heuristic(n)}, f={g[n]+heuristic(n)})")
        # If we reached the goal
        if n == stop_node:
            path = []
            total_cost = g[stop_node]
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('\nPath found: {}'.format(path))
            print('\nTotal cost: {}'.format(total_cost))
            print("g: ",g)
            print()
            print("parent: ",parents)
            
            return path, total_cost

        if Graph_nodes.get(n) is None:
            print('Path does not exist from current noede!!')
            return None, None

        for (m, weight) in get_neighbors(n):
            print(f"Checking neighbor '{m}' with edge weight {weight}")
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
                print(f"  Added '{m}' to open_set with g({m}) = {g[m]}")
            else:
                if g[m] > g[n] + weight:
                    print(f"  Found a better path to '{m}' via '{n}'")
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)
                        print(f"  Moved '{m}' back to open_set")


        open_set.remove(n)
        closed_set.add(n)
        print(f"Moved '{n}' from open_set to closed_set")

    print('Path does not exist!')
    return None, None


def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return []


def heuristic(n):
    H_dist = {
        'A': 13,
        'B': 12,
        'C': 4,
        'D': 7,
        'E': 3,
        'F': 8,
        'G': 2,
        'H': 0
    }
    return H_dist[n]


Graph_nodes = {
    'A': [('B', 2), ('C', 2), ('H', 7)],
    'B': [('D', 4), ('E', 6)],
    'C': [('F', 3), ('G', 2)],
    'F': [('H', 1)],
    'G': [('H', 2)],
}

# Running the A* algorithm from 'A' to 'H'
aStarAlgo('A', 'H')


