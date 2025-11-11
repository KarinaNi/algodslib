def DFS_recursive(node, visited, graph):
    if node not in visited:
        print(node)
        visited[node] = True 
        for nei in graph[node]:
            DFS_recursive(nei, visited, graph)

    return 

# Example usage:
if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0],
        3: [1],
        4: [1, 5],
        5: [4]
    }
    visited = {}
    DFS_recursive(0, visited, graph)

# Expected Output:
# 0
# 1
# 3
# 4         
# 5
# 2