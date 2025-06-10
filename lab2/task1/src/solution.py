from ast import parse

from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory

input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.right = right
        self.left = left


def parse_tree(n, nodes):
    tree = {}
    for i in range(n):
        k, l, r = nodes[i]
        tree[i] = Node(k, l, r)
    return tree


def in_order(tree, root):
    stack = []
    result = []
    node = root

    while stack or node != -1:
        if node != -1:
            stack.append(node)
            node = tree[node].left
        else:
            node = stack.pop()
            result.append(tree[node].key)
            node = tree[node].right

    return result


def pre_order(tree, root):
    if root == -1:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(tree[node].key)

        if tree[node].right != -1:
            stack.append(tree[node].right)
        if tree[node].left != -1:
            stack.append(tree[node].left)

    return result


def post_order(tree, root):
    if root == -1:
        return []

    stack, result = [], []
    last_visited = None
    current = root

    while stack or current != -1:
        if current != -1:
            stack.append(current)
            current = tree[current].left
        else:
            peek_node = stack[-1]
            if tree[peek_node].right != -1 and last_visited != tree[peek_node].right:
                current = tree[peek_node].right
            else:
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
    # Reading input file
    input_data = read_from_file(input_path)

    # Algorithm
    n = input_data[0]
    nodes = input_data[1:]
    result = do_traversals(n, nodes)

    # Writing output file
    output_data = "\n".join(str(x) for x in result)
    write_to_file(output_path, output_data)

if __name__ == "__main__":
    main()