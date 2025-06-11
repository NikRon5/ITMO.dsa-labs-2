from collections import deque
from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory


input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


@measure_time_and_memory
def check_path(n, edges, u, v):
    # Создаем представление графа в виде списка смежности
    graph = [[] for _ in range(n + 1)]

    # Заполняем список
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1) # Массив для отслеживания посещенных вершин
    queue = deque([u]) # Очередь для BFS, начинаем с вершины u
    visited[u] = True # Начальная вершина уже посещенная

    while queue:
        current = queue.popleft()

        # Если достигли целевой вершины, то путь существует
        if current == v:
            return 1

        # Перебираем всех соседей текущей вершины
        for neighbor in graph[current]:
            # Если сосед еще не посещен, то помечаем как посещенный и добавляем в очередь для дальнейшего обхода
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return 0


def main():
    # Чтение входных данных из файла
    input_data = read_from_file(input_path)

    # Извлечение параметров из входных данных
    n, m = input_data[0]
    edges = input_data[1:-1]
    u, v = input_data[-1]

    # Вычисление результата
    result = check_path(n, edges, u, v)

    # Запись результата в выходной файл
    output_data = str(result)
    write_to_file(output_path, output_data)


if __name__ == "__main__":
    main()