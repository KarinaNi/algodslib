from collections import deque
def DFS(adj, source):
    N = len(adj)
    visited = [False]*N
    stack = deque()
    stack.append(source)
    visited[source] = True
    result = []

    while stack:
        current = stack.pop()
        result.append(current)

        print(current)
        for nei in adj[current]:
            if not visited[nei]:
                visited[nei] = True 
                stack.append(nei)

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
    DFS(graph, 0)

# Expected Output:
# 0
# 2
# 1
# 4
# 5
# 3