### Day 8 **Euler Circuit and Path**

An Eulerian Path is a path in a graph that visits every edge exactly once. An Eulerian Circuit is an Eulerian Path which starts and ends on the same vertex. Given an undirected graph with V nodes and E edges, with adjacency list adj, return 2 if the graph contains an Eulerian circuit. If the graph contains an Eulerian path, return 1; otherwise, return 0.

#### Example 1:

**Input:**  
*(Graph data is not provided in the example.)*  
**Output:**  
`2`  
**Explanation:**  
Following is an Eulerian circuit in the mentioned graph:  
1 -> 2 -> 0 -> 1  

#### Example 2:

**Input:**  
*(Graph data is not provided in the example.)*  
**Output:**  
`1`  
**Explanation:**  
Following is an Eulerian path in the mentioned graph:  
1 -> 0 -> 2  

#### Your Task:
You don't need to read or print anything. Your task is to complete the function `isEulerCircuit()` which takes the number of vertices in the graph denoted as V and an adjacency list of the graph denoted as adj and returns 2 if the graph contains an Eulerian circuit. If the graph contains an Eulerian path, it returns 1; otherwise, it will return 0.

- **Expected Time Complexity:** O(V+E) where E is the number of edges in the graph.
- **Expected Space Complexity:** O(V)

**Constraints:**  
- 1 ≤ V, E ≤ 10^4
- 1 ≤ adj[i][j] ≤ V-1
