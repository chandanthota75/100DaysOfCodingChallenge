class Solution:

    def detectCycle(self, num_vertices, adjacency_list):
        
        def find_set(vertex, parent):
            if vertex != parent[vertex]:
                vertex = find_set(parent[vertex], parent)
            return vertex

        def union(x, y, parent, rank):
            x = find_set(x, parent)
            y = find_set(y, parent)
            if rank[x] < rank[y]:
                x, y = y, x
            parent[y] = x
            rank[x] += rank[y]

        parent = [i for i in range(num_vertices)]
        rank = [1 for i in range(num_vertices)]
        visited_edges = set()

        for u in range(num_vertices):
            for v in adjacency_list[u]:
                if (u, v) in visited_edges or (v, u) in visited_edges:
                    continue
                visited_edges.add((u, v))

                u_set = find_set(u, parent)
                v_set = find_set(v, parent)

                if u_set == v_set:
                    return 1

                union(u_set, v_set, parent, rank)
               
        return 0
