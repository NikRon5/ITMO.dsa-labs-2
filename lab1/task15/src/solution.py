from utils.file_utlis import read_from_file, write_to_file
from utils.time_memory_utlis import measure_time_and_memory


input_path = "../txtf/input.txt"
output_path = "../txtf/output.txt"


@measure_time_and_memory
def remove_brackets(s):
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stack = []
    remove = set()

    for i, char in enumerate(s):
        if char in '([{':
            stack.append(i)
        elif char in ')]}':
            if stack and s[stack[-1]] == pairs[char]:
                stack.pop()
            else:
                remove.add(i)

    remove.update(stack)

    result = ''.join(s[i] for i in range(len(s)) if i not in remove)
    return result


def main():
    # Reading input file
    input_data = read_from_file(input_path)

    # Algorithm
    s = input_data
    result = remove_brackets(s)

    # Writing output file
    output_data = result
    write_to_file(output_path, output_data)


if __name__ == "__main__":
    main()