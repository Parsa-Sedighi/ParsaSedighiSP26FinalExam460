"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Parsa Sedighi
Student ID:   133865729

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return " Because it does not calculate the distances between relic chambers themselves and to the end node 'T'. It also skips a few chambers in the path to 'T'.\n" \
    "Decide what path to take in order to reach all of them, while incurring the least cost.\n"\
    "To search and find the order that has the least overall cost from S to T, with all relics collected in between.\n"



# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    # Initialize empty list
    nodes = []
    # Insert spawn to the very begining
    nodes.insert(0, spawn)
    # For each node in relics...
    for n in relics:
        # add the node to the list of nodes
        nodes.append(n)
    nodes = list(set(nodes))
    # Return the list
    return nodes
  

def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    # Initialize a key value pair of all distances (v, w)
    distances = {}
    # For each node in the graph, assign the distance to infinity, since they have not been discovered yet
    for n in graph:
        distances[n] = float('inf')
    # Set the first/start node to 0
    distances[source] = 0

    # A priority queue, containing the cost, source node tuples in it
    pq = [(0, source)]
    # Iterate while there is an availble node in priority queue
    while pq:
        # Pop the current smallest node in the priority queue
        # Assign it to current distance and node u
        cur_distance, u = heapq.heappop(pq)
        # If the current distance is bigger than previously discovered distance for node u...
        if cur_distance > distances[u]:
            # Continue to above line and keep popping until a small current distance is found
            continue
        # Iterate through all neighbors of u
        for v, w in graph.get(u,[]):
            #Update the new distance, add w (weight) and current distance to get to u
            distance = cur_distance + w
            # if the updated distance is less than previous known value of distances
            if distance < distances[v]:
                # Update
                distances[v] = distance
                # push the new node v into the priority queue
                heapq.heappush(pq, (distance,v))

    # Return all distances
    return distances



def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    # First, select the nodes we want to compute every distance for
    nodes = select_sources(spawn, relics, exit_node)
    # Initialze key value pair for all the nodes
    distance_dictionary = {}

    # For each node in source nodes...
    for n in nodes:
        # Run the dijkstra algorithm with the given graph
        distances_for_n = run_dijkstra(graph, n)
        # Store the distances from the source node n in the key value pair for all distances
        distance_dictionary[n] = distances_for_n
    
    # Return the dictionary table containing the precomputed distances from each node
    return distance_dictionary


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return "The computed and stored distance from the source node is absolute (Not subject to change) and the shortest possible path.\n"\
    "The computed and stored distance from the source node is best currently found so far and can be subject to change.\n"\
    "Before iteration, no node has been finalized. So the starting node S is 0, and all other are infinity as temporary values to be explored.\n "\
    "During maintenance, noting nonnegative edge weights, the smallest potential distance popped from priority queue to reach target node u is the absolute shortest. Since all other nodes in priority queue are higher or same value and adding edges weight could only increase distance due to nonnegative property.\n" \
    "Upon termination and when all nodes in priority queue are popped, the invariant has finalized all nodes absolute smallest distances. All infinity valued nodes are treated as unreachable from source node.\n"\
    "Because the route planner relies on accurate distances between each and every node (S, relic chambers, T) to calculate total cost of sequences of routes, and to find the optimal shortest path."


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return "TODO"


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
