graph = {
    'A' : ['B','C','D'],
    'B' : ['G','H'],
    'C' : [],
    'D' : ['E','F'],
    'E' : ['I','J'],
    'F' : [],
    'G' : [],
    'H' : [],
    'I' : [],
    'J' : []
}

visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph,'A')