count = 10

def max_experience(graph, level, position, visited):
    global count

    if level == len(graph):
        return 0

    if (level, position) not in visited:
        visited.add((level, position))

        current_experience = graph[level][position]
        left_experience = max_experience(graph, level + 1, position, visited)
        right_experience = max_experience(graph, level + 1, position + 1, visited)

        count += 1

        return current_experience + max(left_experience, right_experience)
    else:
        return 0

def read_pyramid_from_file(file_path):
    graph = []
    with open(file_path, 'r') as file:
        for line in file:
            row = [int(num) for num in line.split()]
            graph.append(row)
    return graph

def write_result_to_file(result, file_path):
    with open(file_path, 'w') as file:
        file.write(str(result))


pyramid = read_pyramid_from_file('career.in')

#
result = max_experience(pyramid, 0, 0, set())

print(count)



write_result_to_file(result, 'career.out')

