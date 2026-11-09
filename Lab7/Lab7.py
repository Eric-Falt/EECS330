from collections import defaultdict, deque


class Graph:
    """A class to represent a graph using an adjacency list."""

    def __init__(self, directed=False):
        """
        Initializes the graph.
        :param directed: If True, creates a directed graph; otherwise, creates an undirected
        graph.
        """
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v):
        """
        Adds an edge between vertex u and v.
        """
        # Add v to u's list of neighbors.
        # Check for duplicates before adding to prevent parallel edges in the list
        if v not in self.graph[u]:
            self.graph[u].append(v)

        # If it's an undirected graph, add u to v's list of neighbors.
        if not self.directed:
            if u not in self.graph[v]:
                self.graph[v].append(u)

    # --- Question 1: Breadth-First Search (BFS) ---
    def bfs(self, start_node):
        """
        Performs BFS starting from start_node.
        Returns a list of visited nodes in BFS order.
        """
        visited = set([start_node])
        queue = deque([start_node])
        order = []

        while queue:
            current = queue.popleft()
            order.append(current)

            for neighbor in self.graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    # --- Question 2: Depth-First Search (DFS) ---
    def dfs(self, start_node):
        """
        Performs DFS starting from start_node.
        Returns a list of visited nodes in DFS order.
        """
        visited = set()
        order = []

        def visit(node):
            visited.add(node)
            order.append(node)

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visit(neighbor)

        visit(start_node)
        return order


# --- Create Graph Instances for Testing ---
g_undirected = Graph(directed=False)
edges_undirected = [
    ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'E'), ('D', 'F'), ('E', 'C'), ('F', 'C')
]
for u, v in edges_undirected:
    g_undirected.add_edge(u, v)

# --- Test Case 1: Breadth-First Search (BFS) ---
print("--- Test Case 1: Breadth-First Search (BFS) ---")
# Get the BFS result for the undirected graph from 'A'
bfs_result_undirected = g_undirected.bfs('A')
print(f"BFS result of undirected graph from 'A': {bfs_result_undirected}")
print()

# --- Test Case 2: Depth-First Search (DFS) ---
print("--- Test Case 2: Depth-First Search (DFS) ---")
# Get the DFS result for the undirected graph from 'A'
dfs_result_undirected = g_undirected.dfs('A')
print(f"DFS result of undirected graph from 'A': {dfs_result_undirected}")
