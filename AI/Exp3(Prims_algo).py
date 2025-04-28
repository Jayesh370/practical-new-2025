def prim(adjacency_list):
    n = len(adjacency_list)  # Number of nodes
    visited = [False] * n    # To track visited nodes
    mst_weight = 0           # Total weight of MST
    mst_edges = []           # Edges in MST

    def find_min_edge():
        min_weight = float('inf')  # Set initial min_weight to infinity
        min_edge = None            # No edge chosen initially
        for i in range(n):         # Loop through all nodes
            if visited[i]:         # Check if the node has been added to MST
                for j, weight in adjacency_list[i].items():  # Loop through neighbors of the node
                    if not visited[j] and weight < min_weight:  # If neighbor is unvisited and the edge is the smallest so far
                        min_weight = weight   # Update minimum weight
                        min_edge = (i, j, weight)  # Store the edge
        return min_edge  # Return the edge with the smallest weight

    print("\nStarting Prim's Algorithm...\n")
    
    visited[0] = True  # Start with node 0
    print(f"Node 0 added to MST")

    for _ in range(n - 1):  # Repeat n-1 times to add all nodes
        min_edge = find_min_edge()  # Find the edge with the smallest weight
        if min_edge is None:  # If no valid edge was found
            print("No more edges to add. Graph may not be connected.")
            break
        
        u, v, weight = min_edge  # Extract the edge (u -> v) and weight
        print(f"Picked edge ({u} -> {v}) with weight {weight}")

        mst_edges.append(min_edge)  # Add edge to MST
        mst_weight += weight        # Add weight to MST weight
        visited[v] = True           # Mark node v as visited
        print(f"Node {v} added to MST")

    print("\nPrim's Algorithm Completed!")
    print("MST Edges:", mst_edges)
    print("Total MST Weight:", mst_weight)

adjacency_list = [
    {1: 2, 3: 6},        # Node 0 is connected to Node 1 (weight 2), Node 3 (weight 6)
    {0: 2, 2: 3, 3: 8, 4: 5},  # Node 1 is connected to Node 0 (weight 2), Node 2 (weight 3), Node 3 (weight 8), Node 4 (weight 5)
    {1: 3, 4: 7},        # Node 2 is connected to Node 1 (weight 3), Node 4 (weight 7)
    {0: 6, 1: 8, 4: 9},  # Node 3 is connected to Node 0 (weight 6), Node 1 (weight 8), Node 4 (weight 9)
    {1: 5, 2: 7, 3: 9}   # Node 4 is connected to Node 1 (weight 5), Node 2 (weight 7), Node 3 (weight 9)
]

# Run it
if __name__ == "__main__":
    prim(adjacency_list)