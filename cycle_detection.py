def cycle_detection(graph):
    visited = set()
    visiting = set()
    def dfs(node, visited, visiting):
        if node in visiting:
            return True 
        visiting.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei, visited, visiting):
                    return True 
        visiting.remove(node)
        visited.add(node)
        return False 
    
    for node in graph:
        if node not in visited:
            if dfs(node, visited, visiting):
                return True 
    
    return False



# Example usage

if __name__ == "__main__":
    graph_with_cycle = {
        0: [1],
        1: [2],
        2: [0]
    }

    graph_without_cycle = {
        0: [1],
        1: [2],
        2: []
    }

    graph_with_cycle_2 = {
        0: [1,3,5],     
        1: [2],
        2: [0],
        3: [0,5],
        5: [2]
    }
    graph_without_cycle_2 = {
        0: [1], 
        1: [2],
        2: []
    }

    print(cycle_detection(graph_with_cycle))  # Expected Output: True
    print(cycle_detection(graph_without_cycle))  # Expected Output: False   
    print(cycle_detection(graph_with_cycle_2))  # Expected Output: True
    print(cycle_detection(graph_without_cycle_2))  
 
# Expected Output:
# True
# False