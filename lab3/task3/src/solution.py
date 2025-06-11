from collections import deque

from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory

input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


def parse_graph(edges, n):
    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    return graph, in_degree


@measure_time_and_memory
def has_cycle(n, edges):
    graph, in_degree = parse_graph(edges, n)

    queue = deque()
    remaining = n

    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        u = queue.popleft()
        remaining -= 1
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return 1 if remaining > 0 else 0


def main():
    # Reading input file
    input_data = read_from_file(input_path)

    # Algorithm
    n, m = input_data[0]
    edges = input_data[1:]

    result = has_cycle(n, edges)

    # Writing output file
    output_data = str(result)
    write_to_file(output_path, output_data)

if __name__ == "__main__":
    main()