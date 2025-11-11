from collections import deque
def BFS(adj_list,source):
    N = len(adj_list)
    visited = [False]*N
    q = deque()
    q.append(source)
    visited[source] = True
    res = []
    while q:
        current = q.popleft()
        res.append(current)
        print(current)

        for nei in adj_list[current]:
            if not visited[nei]:
                visited[nei] = True 
                q.append(nei)


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
    BFS(graph, 0)

# Expected Output:
# 0
# 1
# 2
# 3 
# 4
# 5