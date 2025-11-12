from collections import deque, defaultdict
def topological_sort_kahns(vertices, edges):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for a, b in edges:
        graph[a].append(b)
        in_degree[b] += 1

    queue = deque()
    for i in range(vertices):
        if in_degree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        current = queue.popleft()
        result.append(current)

        for nei in graph[current]:
            in_degree[nei] -=1

            if in_degree[nei] == 0:
                queue.append(nei)
        
    if len(result)!=vertices:
        return [] # graph has a cycle 
    
    return result

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
    print(topological_sort_kahns(vertices, edges))

# Expected Output:
# [4, 5, 0, 2, 3, 1]
#  or
# [5, 4, 0, 2, 3, 1]
#  or
# [5, 4, 2, 3, 1, 0]
#  or
# [4, 5, 2, 3, 1, 0]            
# or 
# [5, 2, 3, 1, 4, 0]
# or
# [4, 0, 1, 5, 2, 3]
# or
# [5, 0, 2, 3, 1, 4]
# or