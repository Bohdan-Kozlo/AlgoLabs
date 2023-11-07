from collections import deque

graph = {}


def read_file():
    with open("../input.txt", "r") as file:
        for line in file:
            parts = line.strip().split()
            vertex = int(parts[0])
            neighbors = [int(x) for x in parts[1:]]
            graph[vertex] = neighbors


read_file()


def has_cycle(graph):
    visited = set()
    for start in graph:
        if start not in visited:
            queue = deque([(start, None)])
            while queue:
                current, parent = queue.popleft()
                visited.add(current)
                for neighbor in graph[current]:
                    if neighbor != parent:
                        if neighbor in visited:
                            return True
                        queue.append((neighbor, current))
    return False


def write_result():
    with open("../output.txt", "w") as file:
        if has_cycle(graph):
            file.write("True")
        else:
            file.write("False")


write_result()