# Development Log – The Torchbearer

**Student Name:** Parsa Sedighi
**Student ID:**   133865729


---

## Entry 1 – [05/09/2026]: Initial Plan



First, I will draw out the table as provided in Concrete Illustration from ASSIGNMENT.md for better conceptual understanding. Then, I will try to understand why a simple shortest path algorithm alone, or greedy approach is not sufficient and how it fails. I expect the logic to code implementation to be difficult. If one of them is flawed, then the overall solution is not correct. I plan to unit-test my logic and code piece by piece with respect to course material and other sources to direct myself towards a correct solution.

---

## Entry 2 – [05/10/2026]: [Short description]



In the first implementation of function 'run_dijkstra', I did not utilize imported 'heapq', it caused the priority queue to not function as intended by popping the smallest weight first. I fixed this by using the pop function within 'heapq' and it fixed the code logic.

---

## Entry 3 – [05/11/2026]: [Short description]

I revised my answer for part 1 due to wrong assumption. I originally beleieved that a simple shortest path would not work since it does not know distance to T, however it know shortest distance to T, but it would skip few relics. I now understand why relic to relic and final relic to node T distances matter. This way, all relics can be collected from start to end with lowest cost.

---

## Entry 4 – [05/13/2026]: Post-Implementation Reflection



After completing my implementation and passing all test cases, I would like to try different data structures as the placeholder for the relics collected. 
I would like to see how changing the data structure used would require me to change the rest of the implementation.

---

## Final Entry – [05/14/2026]: Time Estimate

Revised the README.md and torchbearer.py to ensure consistency between the two.
Ensuring both files are ready for submission.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 10m|
| Part 2: Precomputation Design | 4H |
| Part 3: Algorithm Correctness | 10m |
| Part 4: Search Design | 10m |
| Part 5: State and Search Space | 4H |
| Part 6: Pruning | 30m |
| Part 7: Implementation | 30m |
| README and DEVLOG writing | 7H |
| **Total** | 16.5H |
