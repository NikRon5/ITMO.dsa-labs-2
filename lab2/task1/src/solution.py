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
    tree = {}
    for i in range(n):
        k, l, r = nodes[i]
        tree[i] = Node(k, l, r)
    return tree


def in_order(tree, root):
    """Центрированный обход дерева (in_order)"""
    stack = [] # Стек для хранения узлов
    node = root # Начинаем с корня
    result = []

    while stack or node != -1:
        if node != -1:
            # Идем до самого левого узла, добавляя все узлы в стек
            stack.append(node)
            node = tree[node].left
        else:
            # Достаем узел из стека и обрабатываем его
            node = stack.pop()
            result.append(tree[node].key)
            # Переходим к правому поддереву
            node = tree[node].right

    return result


def pre_order(tree, root):
    """Прямой обход дерева (pre_order)"""
    if root == -1:
        return []

    stack = [root] # Начинаем с корня
    result = []

    while stack:
        node = stack.pop()
        result.append(tree[node].key)

        # Сначала добавляем правого потомка, чтобы левый обработался первым
        if tree[node].right != -1:
            stack.append(tree[node].right)
        if tree[node].left != -1:
            stack.append(tree[node].left)

    return result


def post_order(tree, root):
    """Обратный обход дерева (post_order)"""
    if root == -1:
        return []

    stack, result = [], []
    last_visited = None # Последний посещенный узел
    current = root # Текущий узел

    while stack or current != -1:
        if current != -1:
            # Идем до самого левого узла
            stack.append(current)
            current = tree[current].left
        else:
            # Смотрим верхний узел в стеке
            peek_node = stack[-1]
            # Если есть правое поддерево и мы его еще не посещали, переходим к нему
            if tree[peek_node].right != -1 and last_visited != tree[peek_node].right:
                current = tree[peek_node].right
            else:
                # Иначе обрабатываем текущий узел
                result.append(tree[peek_node].key)
                last_visited = stack.pop()

    return result


@measure_time_and_memory
def do_traversals(n, nodes):
    tree = parse_tree(n, nodes)

    in_order_res = in_order(tree, 0)
    pre_order_res = pre_order(tree, 0)
    post_order_res = post_order(tree, 0)

    return [in_order_res, pre_order_res, post_order_res]


def main():
    # Чтение входных данных из файла
    input_data = read_from_file(input_path)

    # Извлечение параметров из входных данных
    n = input_data[0]
    nodes = input_data[1:]

    # Вычисление результата
    result = do_traversals(n, nodes)

    # Запись результата в выходной файл
    output_data = "\n".join(str(x) for x in result)
    write_to_file(output_path, output_data)


if __name__ == "__main__":
    main()