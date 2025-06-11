from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory


input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


class Node:
    """Класс для представления узла дерева"""
    def __init__(self, key, left, right):
        self.key = key
        self.right = right
        self.left = left


def parse_tree(n, nodes):
    """Функция для парсинга дерева"""
    tree = {0: None}
    for i in range(1, n + 1):
        k, l, r = nodes[i - 1]
        tree[i] = Node(k, l, r)
    return tree


@measure_time_and_memory
def tree_height(n, nodes):
    if n == 0: return 0

    tree = parse_tree(n, nodes)
    stack = [(1, 1)] # (номер узла, текущая глубина)
    max_height = 1

    while len(stack) != 0:
        i, cur_height = stack.pop()
        node = tree[i] # Получаем узел

        # Обновляем максимальную высоту
        if cur_height > max_height:
            max_height = cur_height

        # Добавляем потомков в стек с увеличенной глубиной (сначала правый, чтобы левый обрабатывался первым)
        if node.right != 0:
            stack.append((node.right, cur_height + 1))
        if node.left != 0:
            stack.append((node.left, cur_height + 1))

    return max_height


def main():
    # Чтение входных данных из файла
    input_data = read_from_file(input_path)

    # Извлечение параметров из входных данных
    n = input_data[0]
    nodes = input_data[1:]

    # Вычисление результата
    result = tree_height(n, nodes)

    # Запись результата в выходной файл
    output_data = str(result)
    write_to_file(output_path, output_data)


if __name__ == "__main__":
    main()