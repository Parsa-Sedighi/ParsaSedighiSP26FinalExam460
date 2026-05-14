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
   
    return """
Because it does not calculate the distances between relic chambers themselves and to the end node 'T'. It also skips a few chambers in the path to 'T'.
Decide what path to take in order to reach all of them, while incurring the least cost.
To search and find the order that has the least overall cost from S to T, with all relics collected in between.
"""


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
    # Add exit node to the end of the list
    nodes.append(exit_node)
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
    return """
The computed and stored distance from the source node is absolute (Not subject to change) and the shortest possible path.

The computed and stored distance from the source node is best currently found so far and can be subject to change.

Before iteration, no node has been finalized.
So the starting node S is 0, and all other are infinity as temporary values to be explored.

During maintenance, noting nonnegative edge weights, the smallest potential distance popped from priority queue to reach target node u is the absolute shortest.
Since all other nodes in priority queue are higher or same value and adding edges weight could only increase distance due to nonnegative property.

Upon termination and when all nodes in priority queue are popped, the invariant has finalized all node's absolute smallest distances.
All infinity valued nodes are treated as unreachable from source node.

Because the Route Planner relies on correct distances between each and every node (S, relic chambers, T) to calculate total cost of sequences of routes, and to find the optimal shortest path. 
"""


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
   
    return """
Picking the immediate lowest cost relic (local optimum) chamber without considering how it may affect the total cost later on, forcing the torchberer into more expensive cost.

| From \ To | B   | C   | D   | T   |
|-----------|-----|-----|-----|-----|
| S         | 1   | 2   | 2   | --  |
| B         | --  | 100 | 1   | 1   |
| C         | 1   | --  | 100 | 100 |
| D         | 1   | 1   | --  | 1   |

Greedy: S -> B -> D -> C -> T with cost of 103
Optimal: S -> C -> B -> D -> T with cost of 4
Greedy fails because it picks the current least expensive travel cost of S -> B instead of S -> C, an oversight which forces the remaining path to be overall expensive.
Algorithm must explore every possible order of nodes that reach destination while visiting all relic chambers.
"""


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
    # Initialize optimal route placeholder to uncomputed fuel cost and empty route
    optimal_route = [float('inf'),[]]

    # Data Structure of my choice to keep track of relics visited: Stack
    relics_visited_order = [] 
    # Set of all relics remaining to visit
    rel_remaining = set(relics)

    # First call to _explore. Pass in precomputed dist_table(Dijkstra), spawn node, 
    # set of relics remainning, stack of rel_collected, accumulted current cost of 0, exit node, placeholder for optimal cost and route
    _explore(dist_table, spawn, rel_remaining, relics_visited_order, 0, exit_node, optimal_route)

    # Return cost at index 0, and optimal route graph at index
    return optimal_route[0], optimal_route[1]



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
    # Pruning condition
    # The prunning is safe because it rejects further branching if the cost incurred so far is equal to or bigger...
    # ...than what is already stored in best. Knowing that global optimal solution can not be achieved further down the line...
    #...since it is a non-negative, directed, weighted graph.
    if best[0] <= cost_so_far:
        return
    
    # Base condition
    # if the relics_remaining is empty, then all relics have been explored by now
    if not relics_remaining:
        # Assign the distance from current node to exit node
        current_cost = dist_table[current_loc][exit_node]
        # Add stored cost so far from previous steps to new distance traveled
        current_cost = cost_so_far + current_cost
        # If the newly accumulated distance is less than what was previously stored...
        if current_cost < best[0]:
            # Assign the new best distance 
            best[0] = current_cost
            # Assign the order of relics in the order they were added
            best[1] = list(relics_visited_order) 
        # Return the function since variables were updated
        return
    
    # Non-base/recursive condition
    # For every remaining relic inside relics_remaining
    for relic in list(relics_remaining):
        # Assign the pre-computed travel cost from current location to that relic
        current_cost = dist_table[current_loc][relic]
        # Remove it from the list of relics remaining since it was just visited.
        relics_remaining.remove(relic)
        # Update the stack of relics visited by appending it to the stack
        relics_visited_order.append(relic)
        # Attain new cost so far by adding the two distances together
        new_cost_so_far = cost_so_far + current_cost
        # Call own recursive function to explore different routes
        _explore(dist_table, relic, relics_remaining, relics_visited_order, new_cost_so_far, exit_node, best)
        
        # Remove the node from the stack of relics_visited
        relics_visited_order.pop()
        # Add the node to remaining relics to be visited
        relics_remaining.add(relic)

    


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
    # Putting the pieces together...
    # Form the distance table by running dijkstra's algorithm and computing distances from all nodes to one another
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    # Find the optimal route between the spawn and exit_node, visiting/collecting all relics using the dist_table and _explore to do so.
    return find_optimal_route(dist_table, spawn, relics, exit_node)


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
