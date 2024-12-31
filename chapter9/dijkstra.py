import math

def find_lowest_cost_node(costs, processed):
    """
    Finds the node with the lowest cost that hasn't been processed yet.

    Args:
        costs (dict): The cost of reaching each node.
        processed (set): Set of nodes that have already been processed.

    Returns:
        str: The node with the lowest cost or None if all nodes are processed.
    """
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def calculate_shortest_path(graph, costs, parents, processed, start, end):
    """
    Calculates the shortest path from the start node to the end node using Dijkstra's algorithm.

    Args:
        graph (dict): The graph represented as an adjacency list.
        costs (dict): The initial costs of reaching each node.
        parents (dict): The initial parent mapping for each node.
        processed (set): Set to track processed nodes.
        start (str): The starting node.
        end (str): The ending node.

    Returns:
        tuple: (cost to the end node, list of nodes in the shortest path)
    """
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.add(node)
        node = find_lowest_cost_node(costs, processed)

    # Backtrack to find the path
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parents[current]
    path.append(start)
    path.reverse()

    return costs[end], path

# Define the graph
graph = {
    "start": {"a": 6, "b": 2},
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {}
}

# Define the hashtables
infinity = math.inf
costs = {"a": 6, "b": 2, "fin": infinity}
parents = {"a": "start", "b": "start", "fin": None}
processed = set()

# Run the algorithm
start_node = "start"
end_node = "fin"
cost, path = calculate_shortest_path(graph, costs, parents, processed, start_node, end_node)

# Display results
print(f"Lowest cost from {start_node} to {end_node}: {cost}")
print(f"Path: {' -> '.join(path)}")