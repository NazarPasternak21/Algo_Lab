from collections import defaultdict
import os


def topological_sort(graph):
    visited = set()
    result = []

    def dfs(node):
        visited.add(node)
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        result.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return result


def main():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(current_directory, "govern.in")

    with open(input_file_path, "r") as file:
        lines = file.readlines()

    dependencies = defaultdict(list)
    reverse_dependencies = set()

    for line in lines:
        tokens = line.split()
        dependencies[tokens[0]].append(tokens[1])
        reverse_dependencies.add(tokens[1])

    result_order = topological_sort(dependencies)

    output_file_path = os.path.join(current_directory, "govern.out")

    with open(output_file_path, "w") as file:
        for doc in result_order:
            file.write(f"{doc}\n")


if __name__ == "__main__":
    main()
