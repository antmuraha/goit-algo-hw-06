from collections import deque

def dfs_recursive(graph, start, end, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path.append(start)
    visited.add(start)

    if start == end:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs_recursive(graph, neighbor, end, path, visited)
            if result:
                return result

    path.pop()
    return None

def bfs_recursive(graph, queue, visited, end):
    if not queue:
        return None

    path = queue.popleft()
    node = path[-1]

    if node in visited:
        return bfs_recursive(graph, queue, visited, end)

    visited.add(node)

    if node == end:
        return path

    for neighbor in graph[node]:
        new_path = list(path)
        new_path.append(neighbor)
        queue.append(new_path)

    return bfs_recursive(graph, queue, visited, end)

# Тестовий граф у вигляді списків суміжності
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Пошук шляху з 'A' до 'F' за допомогою DFS і BFS
start_node = 'A'
end_node = 'F'

queue = deque([[start_node]])
visited = set()

print("Шлях DFS:", dfs_recursive(graph, start_node, end_node))
print("Шлях BFS:", bfs_recursive(graph, queue, visited, end_node))
