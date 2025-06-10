from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory

input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            return
        cur_node = self.root

        while True:
            if key < cur_node.key:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = Node(key)
                    return
            elif key > cur_node.key:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = Node(key)
                    return
            else:
                return

    def find_min(self, key):
        node = self.root
        res = None
        while node:
            if node.key > key:
                res = node
                node = node.left
            else:
                node = node.right
        return res.key if res else 0


@measure_time_and_memory
def do_oparations(operations):
    bst = BinarySearchTree()
    min_keys = []

    for oper in operations:
        to_do = oper[0]
        key = oper[1]

        if to_do == "+":
            bst.insert(key)
        else:
            min_key = bst.find_min(key)
            min_keys.append(min_key)
    return min_keys


def main():
    # Reading input file
    input_data = read_from_file(input_path)

    # Algorithm
    operations = input_data
    result = do_oparations(operations)

    # Writing output file
    output_data = "\n".join(str(x) for x in result)
    write_to_file(output_path, output_data)

if __name__ == "__main__":
    main()