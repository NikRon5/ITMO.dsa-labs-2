from collections import deque

from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory

input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


@measure_time_and_memory
def check_path(n, edges, u, v):
    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    queue = deque([u])
    visited[u] = True

    while queue:
        current = queue.popleft()
        if current == v:
            return 1
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return 0

def main():
    # Reading input file
    input_data = read_from_file(input_path)

    # Algorithm
    n, m = input_data[0]
    edges = input_data[1:-1]
    u, v = input_data[-1]

    result = check_path(n, edges, u, v)

    # Writing output file
    output_data = str(result)
    write_to_file(output_path, output_data)

if __name__ == "__main__":
    main()