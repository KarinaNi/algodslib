
def topological_sort_dfs(V, adj_list):

    def DFS(node, visited, stack, adj):
        visited[node] = True 

        for nei in adj[node]:
            if not visited[nei]:
                DFS(nei, visited, stack, adj)
        
        stack.append(node)

    visited = [False] * V
    stack = []

    for i in range(V):
        if not visited[i]:
            DFS(i, visited, stack, adj_list, )

    stack.reverse()
    return stack

# Example usage:
if __name__ == "__main__":
    vertices = 6
    edges = [
        (5, 2),
        (5, 0),
        (4, 0),
        (4, 1),
        (2, 3),
        (3, 1)
    ]

    # Create adjacency list
    adj_list = [[] for _ in range(vertices)]
    for a, b in edges:
        adj_list[a].append(b)

    print(topological_sort_dfs(vertices, adj_list))
# Expected Output:
# [5, 4, 0, 2, 3, 1]
#  or
# [4, 5, 0, 2, 3, 1]
#  or           
# [5, 4, 2, 3, 1, 0]
# or
# [4, 5, 2, 3, 1, 0]
# or 
# [5, 2, 3, 1, 4, 0]
# or
# [4, 0, 1, 5, 2, 3]
# or
# [5, 0, 2, 3, 1, 4]
# or  
# [4, 0, 1, 2, 3, 5]