### Day 6 **Detect Cycle using DSU**

Given an undirected graph with no self-loops with V (from 0 to V-1) nodes and E edges, the task is to check if there is any cycle in the undirected graph.

Note: Solve the problem using disjoint set union (DSU).

#### Example 1:

**Input:**  
*(Graph data is not provided in the example.)*  
**Output:**  
`1`  
**Explanation:**  
There is a cycle between 0 -> 2 -> 4 -> 0.

#### Example 2:

**Input:**  
*(Graph data is not provided in the example.)*  
**Output:**  
`0`  
**Explanation:**  
The graph doesn't contain any cycle.

#### Your Task:
You don't need to read or print anything. Your task is to complete the function `detectCycle()` which takes the number of vertices in the graph denoting as V and adjacency list adj and returns 1 if the graph contains any cycle, otherwise returns 0.

- **Expected Time Complexity:** O(V + E)
- **Expected Space Complexity:** O(V)

**Constraints:**  
- 2 ≤ V ≤ 10^4
- 1 ≤ E ≤ 10^4
