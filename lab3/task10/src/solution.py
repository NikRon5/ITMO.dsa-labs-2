from collections import deque

from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory

input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


def bellman_ford(n, edges, s):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[s] = 0

    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break
    return dist


def find_negative_cycles(n, edges, adj, dist):
    queue = deque()
    in_queue = [False] * (n + 1)

    for u, v, w in edges:
        if dist[u] != float('inf') and dist[v] > dist[u] + w and not in_queue[v]:
            queue.append(v)
            in_queue[v] = True

    is_neg_inf = [False] * (n + 1)
    while queue:
        u = queue.popleft()
        is_neg_inf[u] = True
        for v in adj[u]:
            if not is_neg_inf[v]:
                queue.append(v)
                is_neg_inf[v] = True
    return is_neg_inf


@measure_time_and_memory
def currency_exchange(n, edges, s):
    adj = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adj[u].append(v)

    dist = bellman_ford(n, edges, s)
    is_neg_inf = find_negative_cycles(n, edges, adj, dist)

    result = []
    for v in range(1, n + 1):
        if dist[v] == float('inf'):
            result.append("*")
        elif is_neg_inf[v]:
            result.append("-")
        else:
            result.append(dist[v])

    return result


def main():
    # Reading input file
    input_data = read_from_file(input_path)

    # Algorithm
    n, m = input_data[0]
    edges = input_data[1:-1]
    s = input_data[-1]

    result = currency_exchange(n, edges, s)

    # Writing output file
    output_data = "\n".join(str(x) for x in result)
    write_to_file(output_path, output_data)

if __name__ == "__main__":
    main()