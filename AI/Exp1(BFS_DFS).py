
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ") #print visited node
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def bfs(visited, graph, node, queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ") #print the visited node
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


def main():
    visited1 = set()  # To keep track of DFS visited nodes
    visited2 = set()  # To keep track of BFS visited nodes
    queue = []  # For BFS
    n = int(input("Enter number of nodes: "))
    graph = dict()

    for i in range(1, n + 1):
        edges = int(input(f"Enter number of edges for node {i}: "))
        graph[i] = list()
        for j in range(1, edges + 1):
            node = int(input(f"Enter edge {j} for node {i}: "))
            graph[i].append(node)

    print("DFS: ", end="")
    dfs(visited1, graph, 1)
    print()
    print("BFS: ", end="")
    bfs(visited2, graph, 1, queue)


if __name__ == "__main__":
    main()

    


# def bfs_recursive(visited, graph, node, queue):
#     if not queue:  # Base condition: if the queue is empty, stop recursion
#         return
    
#     # Pop the first node from the queue
#     s = queue.pop(0)
#     print(s, end=" ")  # Process the node (print it)
    
#     # Explore all the neighbors of the current node
#     for neighbour in graph[s]:
#         if neighbour not in visited:  # If the neighbor hasn't been visited
#             visited.add(neighbour)  # Mark the neighbor as visited
#             queue.append(neighbour)  # Add the neighbor to the queue for future exploration
    
#     # Recur with the updated queue
#     bfs_recursive(visited, graph, node, queue)


 
#     # Initialize visited and queue for BFS (starting from node 1)
#     visited2.add(1)  # Mark the starting node as visited
#     queue.append(1)  # Add the starting node to the queue
#     bfs_recursive(visited2, graph, 1, queue)  # Perform recursive BFS starting from node 1