# The Torchbearer

**Student Name:** Parsa Sedighi
**Student ID:**   133865729
**Course:** CS 460 – Algorithms | Spring 2026


---

## Part 1: Problem Analysis



- **Why a single shortest-path run from S is not enough:**
 Because it does not calculate the distances between relic chambers themselves and to the end node 'T'. It also skips a few chambers in the path to 'T'.

- **What decision remains after all inter-location costs are known:**
 Decide what path to take in order to reach all of them, while incurring the least cost.

- **Why this requires a search over orders (one sentence):**
  To search and find the order that has the least overall cost from S to T, with all relics collected in between.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection


| Starting Node | Why it is a source |
|---|---|
| start node (S) | It must find shortest distance to next chosen relic chamber |
| relic chamber nodes (B,C,D) | It must find all distances to and from all relic chambers to find best overall order  |
| end node (T) | It must be able to end at end node after going through all relic chambers |

### Part 2b: Distance Storage


| Property | Your answer |
|---|---|
| Data structure name | Dictionary/key value pairs |
| What the keys represent | Node |
| What the values represent | minimum distance to reach that node from source |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | A Dictionary allows constant-time look up to values since the length of data does not affect it |

### Part 2c: Precomputation Complexity


- **Number of Dijkstra runs:** 2 + |M| = start node+ end node + set of all relics (positive)
- **Cost per run:** O(E log V), since priority queue was used for V vertices and E Edges.
- **Total complexity:** O((2 + M) * E log V)
- **Justification (one line):** Dijkstra's algorithm is performed for each source, start and end node to calcualte all shortest distances to targets that are reachable.



---

## Part 3: Algorithm Correctness



### Part 3a: What the Invariant Means



- **For nodes already finalized (in S):**
  The computed and stored distance from the source node is absolute (Not subject to change) and the shortest possible path. 

- **For nodes not yet finalized (not in S):**
  The computed and stored distance from the source node is best currently found so far and can be subject to change.

### Part 3b: Why Each Phase Holds


- **Initialization : why the invariant holds before iteration 1:**
  Before iteration, no node has been finalized.
  So the starting node S is 0, and all other are infinity as temporary values to be explored.

- **Maintenance : why finalizing the min-dist node is always correct:**
  During maintenance, noting nonnegative edge weights, the smallest potential distance popped from priority queue to reach target node u is the absolute shortest.
  Since all other nodes in priority queue are higher or same value and adding edges weight could only increase distance due to nonnegative property.

- **Termination : what the invariant guarantees when the algorithm ends:**
  Upon termination and when all nodes in priority queue are popped, the invariant has finalized all node's absolute smallest distances.
  All infinity valued nodes are treated as unreachable from source node.

### Part 3c: Why This Matters for the Route Planner


Because the Route Planner relies on correct distances between each and every node (S, relic chambers, T) to calculate total cost of sequences of routes, and to find the optimal shortest path. 

---

## Part 4: Search Design

### Why Greedy Fails



- **The failure mode:** Picking the immediate lowest cost relic (local optimum) chamber without considering how it may affect the total cost later on, forcing the torchberer into more expensive cost.
- **Counter-example setup:** 
| From \ To | B   | C   | D   | T   |
|-----------|-----|-----|-----|-----|
| S         | 1   | 2   | 2   | --  |
| B         | --  | 100 | 1   | 1   |
| C         | 1   | --  | 100 | 100 |
| D         | 1   | 1   | --  | 1   |
- **What greedy picks:** Greedy: S -> B -> D -> C -> T with cost of 103

- **What optimal picks:** Optimal: S -> C -> B -> D -> T with cost of 4
- **Why greedy loses:** Greedy fails because it picks the current least expensive travel cost of S -> B instead of S -> C, an oversight which forces the remaining path to be overall expensive.

### What the Algorithm Must Explore

Algorithm must explore every possible order of nodes that reach destination while visiting all relic chambers.

---

## Part 5: State and Search Space

### Part 5a: State Representation


| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current_loc | node | Represents the current node the algorithm is currently on|
| Relics already collected | relics_visited_order| Stack | Represents the list of relics collected in the order of most to least recently visited |
| Fuel cost so far | cost_so_far| float | Represents the cumulative cost so far incurred from start to current node.

### Part 5b: Data Structure for Visited Relics


| Property | Your answer |
|---|---|
| Data structure chosen | Stack|
| Operation: check if relic already collected | Time complexity: O(n) |
| Operation: mark a relic as collected | Time complexity: O(1) |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) |
| Why this structure fits | Since Stack allows for last in, first out backtracking, the torchbearer can return to most recent relic chamber/node visited by popping stack |

### Part 5c: Worst-Case Search Space


- **Worst-case number of orders considered:** O(k!)
- **Why:** If there are k number of relics, with all having undirected paths, then the algorithm must find all k! unique orders of visiting them to find the minimum cost. 

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking


- **What is tracked:** The accumulated cost so far incurred and the order of relics which has caused that cost.
- **When it is used:** Whenever the _explore function is called to compare accumulated cost with what is stored in best[0]
- **What it allows the algorithm to skip:** It allows the algorithm to skip exploring the rest of the routes that cannot be more optimal than the current distance. 

### Part 6b: Lower Bound Estimation


- **What information is available at the current state:** At the current state, the final location exit_node (exit_node), updated distances (dist_table), current location (current_loc), and relics to visit (relics_remaining) are available.
- **What the lower bound accounts for:** The optimum cost to traverse from a current relic chamber to another, and also from relic to exit. 
- **Why it never overestimates:** Because it uses distances computed by Dijkstra's algorithm which are garanteed shortest distances between the nodes, therfore it does not overestimated.

### Part 6c: Pruning Correctness


In this case of non-negative, weighted and directed graph, the cost incurred can only increase or remain the same.
If a distance/cost already is bigger or equal to value stored in best, then there is no way for it to be optimal.

---

## References

- Lecture Notes
