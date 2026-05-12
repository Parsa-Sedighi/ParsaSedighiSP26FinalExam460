# The Torchbearer

**Student Name:** Parsa Sedighi
**Student ID:**   133865729
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
 Because it does not calculate the distances between relic chambers themselves and to the end node 'T'. It also skips a few chambers in the path to 'T'.

- **What decision remains after all inter-location costs are known:**
 Decide what path to take in order to reach all of them, while incurring the least cost.

- **Why this requires a search over orders (one sentence):**
  To search and find the order that has the least overall cost from S to T, with all relics collected in between.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Starting Node | Why it is a source |
|---|---|
| start node (S) | It must find shortest distance to next chosen relic chamber |
| relic chamber nodes (B,C,D) | It must find all distances to and from all relic chambers to find best overall order  |
| end node (T) | It must be able to end at end node after going through all relic chambers |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | Dictionary/key value pairs |
| What the keys represent | Node |
| What the values represent | minimum distance to reach that node from source |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Dictionaru allows constant-time loop up to values since the length of data does not affect it  |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** 1 + |R| = start node + set of all relics
- **Cost per run:** O(E log V) since priority queue was used for V vertices and E Edges.
- **Total complexity:** O(|R| * E log V) = O(n^2 log n)
- **Justification (one line):** Dijkstra's algorithm is performed for each source node to calcualte all distances to targets.



---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  The computed and stored distance from the source node is absolute (Not subject to change) and the shortest possible path. 

- **For nodes not yet finalized (not in S):**
  The computed and stored distance from the source node is best currently found so far and can be subject to change.

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  Before iteration, no node has been finalized.
  So the starting node S is 0, and all other are infinity as temporary values to be explored.

- **Maintenance : why finalizing the min-dist node is always correct:**
  During maintenance, noting nonnegative edge weights, the smallest potential distance popped from priority queue to reach target node u is the absolute shortest.
  Since all other nodes in priority queue are higher or same value and adding edges weight could only increase distance due to nonnegative property.

- **Termination : what the invariant guarantees when the algorithm ends:**
  Upon termination and when all nodes in priority queue are popped, the invariant has finalized all nodes absolute smallest distances.
  All infinity valued nodes are treated as unreachable from source node.

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

Because the route planner relies on accurate distances between each and every node (S, relic chambers, T) to calculate total cost of sequences of routes, and to find the optimal shortest path. 

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
