from collections import deque

"""
BFS Shortest Path in Unweighted Graph

Breadth-First Search (BFS) is an algorithm for traversing or searching tree
or graph data structures. It starts at the tree root (or some arbitrary node
of a graph, sometimes referred to as a 'search key') and explores the
neighbor nodes first, before moving to the next level neighbors.

BFS is particularly useful for finding the shortest path in an unweighted graph.

Time Complexity: O(V + E) where V is vertices and E is edges.
Space Complexity: O(V) to store the visited set and queue.
"""


def bfs_shortest_path(graph, start, goal):
    """
    Finds the shortest path from start to goal in an unweighted graph.

    Args:
        graph: Dict representing adjacency list {node: [neighbors]}
        start: Starting node
        goal: Target node

    Returns:
        List representing the path from start to goal, or None if no path exists.
    """
    if start == goal:
        return [start]

    # Queue stores (current_node, path_to_current_node)
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current_node, path = queue.popleft()

        # Get neighbors
        neighbors = graph.get(current_node, [])

        for neighbor in neighbors:
            if neighbor == goal:
                return path + [neighbor]

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


if __name__ == "__main__":
    # Example Graph
    # A -- B -- C
    # |    |    |
    # D -- E -- F
    graph = {
        'A': ['B', 'D'],
        'B': ['A', 'C', 'E'],
        'C': ['B', 'F'],
        'D': ['A', 'E'],
        'E': ['B', 'D', 'F'],
        'F': ['C', 'E']
    }

    start_node = 'A'
    goal_node = 'F'
    path = bfs_shortest_path(graph, start_node, goal_node)
    
    print(f"Graph: {graph}")
    print(f"Shortest path from {start_node} to {goal_node}: {path}")
