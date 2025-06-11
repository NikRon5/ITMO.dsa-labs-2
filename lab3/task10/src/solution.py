from collections import deque
from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory


input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


def bellman_ford(n, edges, s):
    """Алгоритм Беллмана-Форда для нахождения кратчайших путей из вершины s"""
    dist = [float('inf')] * (n + 1) # Инициализация расстояний бесконечностью
    dist[s] = 0  # Расстояние до начальной вершины = 0

    # Релаксация всех ребер (n - 1) раз
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            # Если найден более короткий путь через вершину u
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                updated = True
        # Если не было обновлений, то выходим раньше
        if not updated:
            break
    return dist


def find_negative_cycles(n, edges, adj, dist):
    """Поиск вершин, достижимых из отрицательных циклов"""

    queue = deque()
    in_queue = [False] * (n + 1)

    # Находим вершины, которые можно улучшить после (n-1) итераций
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[v] > dist[u] + w and not in_queue[v]:
            queue.append(v)
            in_queue[v] = True

    is_neg_inf = [False] * (n + 1)

    # Распространяем метки о достижимости из отрицательных циклов
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
    # Строим список смежности для графа
    adj = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adj[u].append(v)

    dist = bellman_ford(n, edges, s)
    is_neg_inf = find_negative_cycles(n, edges, adj, dist)

    result = []
    for v in range(1, n + 1):
        if dist[v] == float('inf'):
            result.append("*") # Пути не существует
        elif is_neg_inf[v]:
            result.append("-") # Путь есть, но кратчайшего нет]
        else:
            result.append(dist[v]) # Кратчайший путь

    return result


def main():
    # Чтение входных данных из файла
    input_data = read_from_file(input_path)

    # Извлечение параметров из входных данных
    n, m = input_data[0]
    edges = input_data[1:-1]
    s = input_data[-1]

    # Вычисление результата
    result = currency_exchange(n, edges, s)

    # Запись результата в выходной файл
    output_data = "\n".join(str(x) for x in result)
    write_to_file(output_path, output_data)


if __name__ == "__main__":
    main()