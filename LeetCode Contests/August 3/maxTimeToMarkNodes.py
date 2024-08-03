from collections import deque

def timetaken(edges):
    # Build the adjacency list representation of the tree
    n = len(edges) + 1
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Function to calculate marking time starting from each node
    def bfs_marking_time(start):
        # Initialize the queue with the starting node and its marking time
        queue = deque([(start, 0)])
        seen = {start}
        mark_times = [-1] * n
        mark_times[start] = 0
        
        while queue:
            node, time = queue.popleft()
            
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    # Determine the next time increment based on the node's number
                    next_time = time + (1 if neighbor % 2 else 2)
                    mark_times[neighbor] = next_time
                    queue.append((neighbor, next_time))
        
        return max(mark_times)
    
    # Calculate the marking time for each node being the starting point
    times = [bfs_marking_time(i) for i in range(n)]
    return times

# Example test cases
edges1 = [[0,1],[0,2]]
edges2 = [[0,1]]
edges3 = [[2,4],[0,1],[2,3],[0,2]]

print(timetaken(edges1))  # Output: [2, 4, 3]
print(timetaken(edges2))  # Output: [1, 2]
print(timetaken(edges3))  # Output: [4, 6, 3, 5, 5]